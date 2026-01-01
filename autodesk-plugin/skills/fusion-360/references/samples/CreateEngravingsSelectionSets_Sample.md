# Create Engravings Selection Sets API Sample

## Description

This sample script demonstrates how to find and machine engravings in the Z+ direction using pocket recognition.

The script will first open an example model via its URN. Using pocket recognition, it will identify pockets that may be engravings based on their dimensions.

We assume here that an engraving pocket is:

* Made with a flat bottom face and no fillet.
* A closed pocket.
* Have a Z height less than 2 mm

We demonstrate creating selection sets in both design and manufacture workspaces and use one of the selection sets as an operation geometry selection input to generate an engraving operation.

The engraving toolpath can be seen by expanding the setup and selecting the operation.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, adsk.cam, traceback

PROJECT_URN = 'urn:adsk.wipprod:fs.file:vf.XhO3KCCLTUi83YJLaAiCRg?version=1'
TOOL_LIBRARY_URN = 'systemlibraryroot://Samples/Milling Tools (Metric).json'

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Open document by its URN.
        doc = loadProjectFromURN(PROJECT_URN)
        if doc is None:
            return

        # Switch to the manufacturing space.
        camWS = ui.workspaces.itemById('CAMEnvironment')
        camWS.activate()

        # Get the cam product.
        products = doc.products
        cam: adsk.cam.CAM = products.itemByProductType('CAMProductType')

        # Get the design product.
        design: adsk.fusion.Design = products.itemByProductType('DesignProductType')

        ############# Find design and manufacturins bRepBodies #############

        # Get the first body of the design root component.
        designBody = design.rootComponent.bRepBodies.item(0)

        # Find the equivalent body in manufacturing space.
        comp = designBody.parentComponent
        camBody: adsk.fusion.BRepBody = None
        for body in cam.designRootOccurrence.bRepBodies:
            if body.parentComponent.name == comp.name:
                camBody = body
                break

        ############# Find engravings using pocket recognition #############

        # Define recognition vector: recognize pockets on top side (Z- view direction).
        searchVector = adsk.core.Vector3D.create(0, 0, -1)

        # Recognize any pockets in the design body.
        recognizedPockets = adsk.cam.RecognizedPocket.recognizePockets(designBody, searchVector)

        # Identify pockets that may be engravings based on their dimensions.
        # We assume here that an engraving pocket is:
        #  - made of a flat bottom face (no fillet or such)
        #  - must be a closed pocket
        #  - Z height is less than 2 mm
        POCKET_MAX_DEPTH = 0.2

        engravingFeatures: list[EngravingFeature] = []
        for recognizedPocket in recognizedPockets:
            # Pocket must be closed.
            if recognizedPocket.isClosed:
                # Check the pocket depth.
                if recognizedPocket.depth <= POCKET_MAX_DEPTH:
                    # Look only at flat types.
                    if recognizedPocket.bottomType == adsk.cam.RecognizedPocketBottomType.RecognizedPocketBottomTypeFlat:
                        # This pocket matches the requirements so adding it as an engraving.
                        engraving = EngravingFeature(designBody, recognizedPocket, searchVector)
                        engravingFeatures.append(engraving)

        ############# Create selections sets in design space #############

        # Create a list of all engraved bottom faces from design body.
        bottomFaces: list[adsk.fusion.BRepFace] = []
        for engraving in engravingFeatures:
            bottomFaces.extend(engraving.bottomFaces)

        # Add into the design space
        design.selectionSets.add(bottomFaces, '(design) Engravings bottom faces (all)')

        ############# Create selections sets in manufacturing space #############

        # Find the equivalent BRep face in the manufacturing space using tempID.
        bottomFacesInCam = findEquivalentFacesInManufacturingSpace(camBody, bottomFaces)
        # Add into the manufacturing space, using this selection set as operation geometry selection input also.
        engravingsBottomFacesSelectionSet = cam.selectionSets.add(bottomFacesInCam, '(cam) Engravings bottom faces (all)')

        ############# Create an operation using selections set data #############

        # Create a basic setup.
        setupInput = cam.setups.createInput(adsk.cam.OperationTypes.MillingOperation)
        setupInput.name = 'Sample setup with engraving operation'
        setupInput.models = [camBody]
        setup = cam.setups.add(setupInput)

        # Find an engraving tool from tool library using a query.
        toolLibraries = adsk.cam.CAMManager.get().libraryManager.toolLibraries
        url = adsk.core.URL.create(TOOL_LIBRARY_URN)
        toolLibrary = toolLibraries.toolLibraryAtURL(url)
        query = toolLibrary.createQuery()
        query.criteria.add('tool_type', adsk.core.ValueInput.createByString('chamfer mill'))
        query.criteria.add('tool_diameter.min', adsk.core.ValueInput.createByReal(0.4)) # 4 mm
        query.criteria.add('tool_diameter.max', adsk.core.ValueInput.createByReal(0.6)) # 6 mm
        results = query.execute()
        tools: list[adsk.cam.Tool] = []
        for result in results:
            tools.append(result.tool)
        engravingTool = tools[0] # We pick the first tool found.

        # Create an engraving operation.
        operationInput = setup.operations.createInput('engrave')
        operationInput.tool = engravingTool
        operationInput.displayName = 'Engraving Operation'
        operationInput.parameters.itemByName('topHeight_offset').expression = '1 mm'

        # Add the selection set data to the operationInput as a new face contour selection entry.
        cadContours2dParam: adsk.cam.CadContours2dParameterValue = operationInput.parameters.itemByName('contours').value
        curveSelections = cadContours2dParam.getCurveSelections()
        chain = curveSelections.createNewFaceContourSelection()
        chain.inputGeometry = engravingsBottomFacesSelectionSet.entities
        cadContours2dParam.applyCurveSelections(curveSelections)

        # Add the operationInput to the setup.
        setup.operations.add(operationInput)
        setup.operations.item(setup.operations.count-1).isLightBulbOn = True

        # Generate operation.
        cam.generateAllToolpaths(True)

        # Raise a done! message.
        ui.messageBox('- Selection Sets have been created in both design and manufacturing workspaces.\n' + \
                        '- An engraving operation has been created.',
                        'Fusion' + '\t' * 6, # Widen the messageBox width
                        adsk.core.MessageBoxButtonTypes.OKButtonType,
                        adsk.core.MessageBoxIconTypes.InformationIconType)

    except Exception as e:
        if ui:
            ui.messageBox(f'Failed: {e}\n{traceback.format_exc()}', 'Fusion',
                            adsk.core.MessageBoxButtonTypes.OKButtonType,
                            adsk.core.MessageBoxIconTypes.CriticalIconType)

def findEquivalentFacesInManufacturingSpace(camBody: adsk.fusion.BRepBody, designFaces: list[adsk.fusion.BRepFace]):
    ''' From given list of design faces, find the equivalent faces in a cam body using tempID '''
    camFaces: list[adsk.fusion.BRepFace] = []
    for face in designFaces:
        items = camBody.findByTempId(face.tempId)
        for item in items:
            if isinstance(item, adsk.fusion.BRepFace):
                camFaces.append(item)
    return camFaces

############# Engraving pocket feature object #############

class EngravingFeature():
    ''' Engraving pocket feature object (that can deal with bottom and wall faces extraction) '''
    def __init__(self, body: adsk.fusion.BRepBody, recognizedPocket: adsk.cam.RecognizedPocket, searchVector: adsk.core.Vector3D):
        self.__body = body
        self.__recognizedPocket = recognizedPocket
        self.__searchVector = searchVector
        self.__component = self.__body.parentComponent
        self.__wallFaces: list[adsk.fusion.BRepFace] = []
        self.__bottomFaces: list[adsk.fusion.BRepFace] = []
        # Extract the bottom and top faces when the object is created.
        self.__extractFaces()

    @property
    def wallFaces(self):
        ''' Return engraving pocket wall faces '''
        return self.__wallFaces

    @property
    def bottomFaces(self):
        ''' Return engraving pocket bottom faces '''
        return self.__bottomFaces

    def __extractFaces(self):
        ''' Extract pocket bottom and wall faces '''
        boundaries = self.__recognizedPocket.boundaries
        islands = self.__recognizedPocket.islands

        # Get the pocket boundary key points.
        points: list[adsk.core.Point3D] = []
        for boundary in boundaries:
            boundaryPoints = self.__getPointsFromCurve3DPath(boundary)
            points.extend(boundaryPoints)

        # Get any pocket island key points.
        for island in islands:
            islandPoints = self.__getPointsFromCurve3DPath(island)
            points.extend(islandPoints)

        # Extract the faces.
        self.__wallFaces = self.__getWallFaces(points)
        self.__bottomFaces = self.__getBottomFaces(points)

    def __getPointsFromCurve3DPath(self, curves: adsk.core.Curve3DPath):
        ''' Get a list of exact points on the curve 3D paths '''
        points: list[adsk.core.Point3D] = []
        for curve in curves:
            # Cast to get the actual segment type as casting returns None if the wrong object is passed.
            line3D = adsk.core.Line3D.cast(curve)
            arc3D = adsk.core.Arc3D.cast(curve)
            circle3D = adsk.core.Circle3D.cast(curve)
            ellipse3D = adsk.core.Ellipse3D.cast(curve)
            nurbsCurve3D = adsk.core.NurbsCurve3D.cast(curve)
            ellipticalArc3D = adsk.core.EllipticalArc3D.cast(curve)

            nurbs: adsk.core.NurbsCurve3D = None
            if line3D:
                nurbs = line3D.asNurbsCurve
            elif arc3D:
                nurbs = arc3D.asNurbsCurve
            elif circle3D:
                nurbs = circle3D.asNurbsCurve
            elif ellipse3D:
                nurbs = ellipse3D.asNurbsCurve
            elif nurbsCurve3D:
                nurbs = nurbsCurve3D.copy()
            elif ellipticalArc3D:
                nurbs = ellipticalArc3D.asNurbsCurve
            else:
                classType = curve.classType()
                raise Exception('Unsupported curve type: ' + classType)

            if nurbs:
                _, startPoint, endPoint = nurbs.evaluator.getEndPoints()
                # There is no need to add the end point as the start of the end of the curve is the start of the next one...
                points.append(startPoint)

        return points

    def __getBottomFaces(self, points: list[adsk.core.Point3D]):
        ''' Search the pocket bottom faces using the provided boundary points '''
        faces: list[adsk.fusion.BRepFace] = []
        for point in points:
            breps = self.__component.findBRepUsingPoint(point, adsk.fusion.BRepEntityTypes.BRepFaceEntityType, -1, True)
            for brep in breps:
                # Cast so we have a nicely typed object.
                brep = adsk.fusion.BRepFace.cast(brep)
                # Filter to find only the wall faces where the normal is parallel to the search vector.
                _ , normal = brep.evaluator.getNormalAtPoint(brep.pointOnFace)
                if normal.isParallelTo(self.__searchVector):
                    if not brep in faces:
                        faces.append(brep)
        return faces

    def __getWallFaces(self, points: list[adsk.core.Point3D]):
        ''' Search the pocket wall faces using the provided boundary points '''
        faces: list[adsk.fusion.BRepFace] = []
        for point in points:
            breps = self.__component.findBRepUsingPoint(point, adsk.fusion.BRepEntityTypes.BRepFaceEntityType, -1, True)
            for brep in breps:
                # Cast so we have a nicely typed object.
                brep = adsk.fusion.BRepFace.cast(brep)
                # Filter to find only the wall faces where the normal is perpendicular to the search vector.
                _ , normal = brep.evaluator.getNormalAtPoint(brep.pointOnFace)
                if normal.isPerpendicularTo(self.__searchVector):
                    if not brep in faces:
                        faces.append(brep)
        return faces

def loadProjectFromURN(urn:str = None) -> adsk.core.Document:
    ''' Minimal self-contained function to load and return a document via URN or return None safely '''
    doc: adsk.core.Document = None
    app = adsk.core.Application.get()
    if urn is not None:
        try: # File not found causes an exception
            project: adsk.core.DataFile = app.data.findFileById(urn)
            if project:
                doc = app.documents.open(project, True)
            else:
                app.userInterface.messageBox(f'File not found for URN: {urn}!')
        except Exception as e:
            if str(e)[0:38] == '3 : Design is located in another team.':
                # Although the document has been loaded, variable 'doc' may not be populated
                if doc is None:
                    doc: adsk.core.Document = adsk.core.Application.get().activeDocument
            elif str(e)[0:20] == '3 : file not found':
                app.userInterface.messageBox(f'File not found for URN: {urn}!')
            else:
                # Abandon for unhandled errors, displaying the error message.
                app.userInterface.messageBox(f'Failed:{str(e)}\n{traceback.format_exc()}')
    return doc
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |