# Create Setups From Hole Recognition API Sample

## Description

This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.

The Fusion Manufacturing Extension is required for Hole Recognition.

The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector.

## Code Samples

* [Python](#Python)

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, adsk.cam, traceback, math

#################### Global settings ####################
_app = adsk.core.Application.get()
_ui = _app.userInterface

# A Constant that sets the vector output to 6 decimal places.
DECIMAL_PLACES = 6

# The name of the part for which we create a reference setup.
BODY_NAME = 'Body999'

# Names of any fixtures.
FIXTURE_NAMES: list[str] = ['5 Axis-V562-VPY56:1', 'Component30:1']

# Our sample model, 3 way coupling part + Fixture.
PROJECT_URN = 'urn:adsk.wipprod:fs.file:vf.9Y50bpnXR-eWplz5h8SAYg?version=1'

# If True, print results of hole information to the TEXT COMMAND window of Fusion.
PRINT_RESULTS = True

#################### Script entry point ####################
def run(context):
    ''' Main entry point for the script. '''
    try:
        #################### Initialisation #####################

        doc = loadProjectFromURN(PROJECT_URN)
        if doc is None: return

        # Switch to the manufacturing workspace (CAM environment).
        camWS = _ui.workspaces.itemById('CAMEnvironment')
        camWS.activate()

        # Get the CAM product.
        products = doc.products
        cam: adsk.cam.CAM = products.itemByProductType("CAMProductType")

        # Get the CAD product.
        design: adsk.fusion.Design = products.itemByProductType('DesignProductType')

        #################### Get body or component ####################
        part = getBRepBodyByName(design, BODY_NAME)
        if not part:
            userMessageBox(f'{BODY_NAME} not found in the Fusion document', True)
            return

        #################### Reference Setup ####################

        # Create a reference setup based on the sample part.
        referenceSetup = createReferenceSetup(design, cam, part)

        # The Fusion Manufacturing Extension is required  for hole recogintion.
        if not isManufacturingExtensionActive(referenceSetup):
            userMessageBox('Fusion Manufacturing Extension is required for hole recognition.', True)
            return

        #################### Define Z Vectors ####################
        # Create a list of vectors for each hole group from which setups will be generated.
        zVectors = getVectorsFromRecognziedHoles(part)

        # Create a dummy anchor component.
        # This is required if the default option:
        # 'First component grounded to parent' is ticked in Preferences > Design > Assemblies.
        occurrence, component = createComponent(design, 'dummyAnchorComponent')

        # Use a list to store the created setups.
        createdSetups: list[adsk.cam.Setup] = []

        #################### Loop to Create Setups for Each Z Vector ####################
        for vector in zVectors:

            # Generate a name string based on the vector.
            name = createStringFromVector(vector)

            # Create a new component.
            newOccurrence, newComponent = createComponent(design, name)

            # Transform if it's not vertical.
            if not vector.isEqualTo(adsk.core.Vector3D.create(0, 0, 1)):
                transformMatrix = getTransformMatrixFromVector(vector)
                transformComponent(transformMatrix, newOccurrence, design)

            newSetup = createNewSetupFromReference(cam, referenceSetup, name)

            axisX, axisY, origin = getComponentAxes(newComponent, newOccurrence)
            newSetup = applyAxesToSetup(axisX, axisY, origin, newSetup)

            createdSetups.append(newSetup)

        _app.log(f'---Completed Creation of {len(createdSetups)} Setup{'s' if len(createdSetups) > 1 else ''}---')
        userMessageBox('Completed. Please expand Setups to view the new setups.', False)

    except Exception as e:
        userMessageBox(f'Failed:{e}\n{traceback.format_exc()}', True)

#################### Custom Axes Setup Creation Functions ####################

def createComponent(design: adsk.fusion.Design, name: str):
    '''
    Creates a new component in the design and names it.
    Returns the occurrence and the component.
    '''
    rootComp = design.rootComponent
    occurrence = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    component = occurrence.component
    component.name = f'setVector: {name}'
    return occurrence, component

def transformComponent(transformMatrix: adsk.core.Matrix3D, occurrence: adsk.fusion.Occurrence, design: adsk.fusion.Design):
    ''' Transforms the given occurrence using the provided transformation matrix. '''
    try:
        occurrence.transform2 = transformMatrix
        design.snapshots.add()

    except Exception as e:
        if str(e)[0:35] != '3 : this is not a parametric design': # We handle this specific error.
            # Abandon for unhandled errors, displaying the error message.
            userMessageBox(str(e), True)
            return

def getComponentAxes(component: adsk.fusion.Component, occurrence: adsk.fusion.Occurrence):
    ''' Retrieves the X and Y axes and origin point of the given component in the assembly context. '''
    axisX = component.xConstructionAxis.createForAssemblyContext(occurrence)
    axisY = component.yConstructionAxis.createForAssemblyContext(occurrence)
    origin = component.originConstructionPoint.createForAssemblyContext(occurrence)
    return axisX, axisY, origin

def createNewSetupFromReference(cam: adsk.cam.CAM, referenceSetup: adsk.cam.Setup, setupName: str):
    ''' Duplicates a reference setup and renames it based on the given setup name. '''
    setups = cam.setups

    # Duplicate the reference setup.
    duplicateSetup = referenceSetup.duplicate()

    # Move the duplicated setup after the last one.
    if duplicateSetup:
        newSetup = setups[1]
        newSetup.moveAfter(setups[-1])
    else:
        userMessageBox('Failed to duplicate setup', True)

    # Set stock mode to previous setup and rename the new setup.
    newSetup.parameters.itemByName('job_stockMode').expression = "'previoussetup'"
    newSetup.name = f'Setup {setupName}'
    return newSetup

def createStringFromVector(vector: adsk.core.Vector3D):
    '''Converts a vector to a string for naming purposes.'''
    # Adding zero so a -0.0 will become 0.0 (nicer for printing a zero value).
    x = round(vector.x, DECIMAL_PLACES) + 0
    y = round(vector.y, DECIMAL_PLACES) + 0
    z = round(vector.z, DECIMAL_PLACES) + 0
    vectorString = f'[{x}, {y}, {z}]'
    return vectorString

def applyAxesToSetup(axisX: adsk.fusion.ConstructionAxis, axisY: adsk.fusion.ConstructionAxis, \
                     origin: adsk.fusion.ConstructionPoint, setup: adsk.cam.Setup):
    ''' Applies the given axes and origin to the WCS of the setup. '''
    setup.parameters.itemByName('wcs_orientation_mode').expression = "'axesXY'"

    # Apply the input X and Y axes to the setup.
    axisXSelection: adsk.cam.CadObjectParameterValue = setup.parameters.itemByName('wcs_orientation_axisX').value
    axisXSelection.value = [axisX]
    axisYSelection: adsk.cam.CadObjectParameterValue = setup.parameters.itemByName('wcs_orientation_axisY').value
    axisYSelection.value = [axisY]

    # Apply the origin point to the setup.
    setup.parameters.itemByName('wcs_origin_mode').expression = "'point'"
    originSelection: adsk.cam.CadObjectParameterValue = setup.parameters.itemByName('wcs_origin_point').value
    originSelection.value = [origin]
    return setup

def getTransformMatrixFromVector(zVector: adsk.core.Vector3D):
    ''' Generates a transformation matrix based on a Z vector. '''
    zVector.normalize()

    # Define an initial X vector.
    xVector = adsk.core.Vector3D.create(1, 0, 0)

    # If the Z vector is too close to the X vector, use Y as an alternative.
    if abs(zVector.angleTo(xVector)) < math.radians(1):
        xVector = adsk.core.Vector3D.create(0, 1, 0)

    # Compute the orthogonal Y vector.
    yVector = zVector.crossProduct(xVector)
    yVector.normalize()

    # Recompute the orthogonal X vector.
    xVector = yVector.crossProduct(zVector)
    xVector.normalize()

    # Create the transformation matrix.
    transformMatrix = adsk.core.Matrix3D.create()
    transformMatrix.setWithCoordinateSystem(adsk.core.Point3D.create(0, 0, 0), xVector, yVector, zVector)
    return transformMatrix

#################### Helper Functions ####################

def getBRepBodyByName(design: adsk.fusion.Design, name: str):
    ''' Get a body by its name (return None if not found) '''

    for i in range(design.rootComponent.bRepBodies.count):
        body = design.rootComponent.bRepBodies.item(i)
        if body.name == name:
            return body

    for i in range(design.rootComponent.allOccurrences.count):
        occ = design.rootComponent.allOccurrences.item(i)
        for j in range(occ.bRepBodies.count):
            body = occ.bRepBodies.item(j)
            if body.name == name:
                return body
    return None

def isManufacturingExtensionActive(setup: adsk.cam.Setup):
    ''' Checks if manufacturing extension is active '''
    for op in setup.operations.compatibleStrategies:
        if op.name == 'steep_and_shallow':
            # The Fusion Manufacturing Extension is required for Hole Recogintion.
            if op.isGenerationAllowed:
                return True
            else:
               return False
    return False

def userMessageBox(messageText: str, isWarning: bool = False):
    ''' Keep messageBox calls informative but succinct'''
    iconType = adsk.core.MessageBoxIconTypes.WarningIconType if isWarning else adsk.core.MessageBoxIconTypes.InformationIconType
    _ui.messageBox(messageText, 'Fusion\t\t\t\t\t\t', adsk.core.MessageBoxButtonTypes.OKButtonType, iconType) # Title tabs widen messageBox.

def createReferenceSetup(design: adsk.fusion.Design, cam: adsk.cam.CAM, part: adsk.fusion.BRepBody):
    ''' Creates a reference setup with a simple stock mode and offsets. '''
    setups = cam.setups
    setupInput = setups.createInput(adsk.cam.OperationTypes.MillingOperation)

    # Add the part to the setup input models.
    models = [part]
    setupInput.models = models

    # Add fixture items into the setup.
    modelsOther: list[adsk.fusion.Occurrence] = []
    for fixtureName in FIXTURE_NAMES:
        modelsOther.append(design.rootComponent.allOccurrences.itemByName(fixtureName))

    setupInput.fixtures = modelsOther

    # Create the setup and configure stock properties.
    setup = setups.add(setupInput)
    setup.name = 'Setup Reference'
    setup.stockMode = adsk.cam.SetupStockModes.RelativeBoxStock

    # Configure stock offsets.
    setup.parameters.itemByName('job_stockOffsetMode').expression = "'simple'"
    setup.parameters.itemByName('job_stockOffsetSides').expression = '0 mm'
    setup.parameters.itemByName('job_stockOffsetTop').expression = '1 mm'
    return setup

def isVectorInListOfVectors(vector: adsk.core.Vector3D, vectors: list[adsk.core.Vector3D]):
    ''' Check if the vector is already in a list of vectors '''
    for v in vectors:
        if vector.isEqualTo(v):
            return True
    return False

def getVectorsFromRecognziedHoles(part: adsk.fusion.BRepBody):
    ''' Hole Recognition of body in documnent and extract vectors '''
    vectors: list[adsk.core.Vector3D] = []

    # The Fusion Manufacturing Extension is required for Hole Recogintion.
    recognizedHolesInput = adsk.cam.RecognizedHolesInput.create()
    holeGroups = adsk.cam.RecognizedHoleGroup.recognizeHoleGroupsWithInput([part], recognizedHolesInput)
    holes = adsk.cam.RecognizedHole.recognizeHoles([part])
    if PRINT_RESULTS:
        _app.log(f'Hole Group count = {holeGroups.count} (Additional groups are created for differing hole types sharing the same orientation)')
        _app.log(f'Total number of holes in model = {holes.count}')
    grpNum = 0

    # Deal with hole groups.
    for holeGroup in holeGroups:
        grpNum += 1
        hole = holeGroup.item(0) # This is the first hole in the group.
        axis = hole.axis
        if PRINT_RESULTS:
            strVect = createStringFromVector(hole.axis)
            _app.log(f'Number of holes in group {grpNum} = {holeGroup.count} : Vector direction = {strVect}')

        # We make sure the vector is not added to the Fusion Setup list if it's a duplicate.
        if not isVectorInListOfVectors(axis, vectors):
            vectors.append(axis)

    _app.log('***Completed hole recognition***')
    return vectors

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