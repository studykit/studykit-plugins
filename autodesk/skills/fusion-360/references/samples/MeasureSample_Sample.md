# Measure Sample

## Description

Measure related functions

## Code Samples

* [Python](#Python)
* [C++](#C++)

|  |
| --- |
| Copy Code |

```
#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def validate(discription, result, baseline):
    if type(result) is str:
        if result != baseline:
            raise Exception(discription + ' is different!\n'
                           + 'Result is ' + result + '\n'
                           + 'Baseline is ' + baseline + '\n'
                           )
    elif type(result) is float:
        if abs(result - baseline) > 10e-6:
            raise Exception(discription + ' is different!\n'
                           + 'Result is ' + str(result) + '\n'
                           + 'Baseline is ' + str(baseline) + '\n'
                           )
    elif type(result) is bool:
        if result != baseline:
            raise Exception(discription + ' is different!\n'
                           + 'Result is ' + str(result) + '\n'
                           + 'Baseline is ' + str(baseline) + '\n'
                           )
    else:
        raise Exception('Validaion is not support the data type ' + discription)
#endTest

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Create a new document
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the root component of the active design
        rootComp = design.rootComponent

        # Create a sketch
        sketches = rootComp.sketches
        sketch1 = sketches.add(rootComp.yZConstructionPlane)

        # Create sketch lines
        sketchLines = sketch1.sketchCurves.sketchLines

        # Create some 3D points
        point1 = adsk.core.Point3D.create(0.0, 0.0, 0.0)
        point2 = adsk.core.Point3D.create(5.0, 5.0, 0.0)

        # Create sketch rectangle
        sketchLines.addTwoPointRectangle(point1, point2)

        # Get the profile
        profile = sketch1.profiles.item(0)

        # Create an extusion input
        extrudes = rootComp.features.extrudeFeatures
        extrudeInput = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Set extrude distance is 6 cm
        distance = adsk.core.ValueInput.createByReal(6.0)
        # Set the distance extent
        extrudeInput.setDistanceExtent(False, distance)
        # Set the extrude type is solid
        extrudeInput.isSolid = True

        # Create the extrude
        extrude = extrudes.add(extrudeInput)

        # Get the extrude brepbody
        brepBody = extrude.bodies.item(0)

        # Measure minimum distance
        print("*** Measure minimum distance.")
        sketchLine = sketchLines.item(0)
        brepEdge = brepBody.edges.item(0)
        measureResult = app.measureManager.measureMinimumDistance(sketchLine, brepEdge)
        minDistance = measureResult.value
        print('Minimum distance value is ' + str(minDistance))

        position1 = measureResult.positionOne
        position2 = measureResult.positionTwo
        print('positionOne is ('
              + str(position1.x)
              + ','
              + str(position1.y)
              + ','
              + str(position1.z)
              + ')'
             )
        print('positionTwo is ('
              + str(position2.x)
              + ','
              + str(position2.y)
              + ','
              + str(position2.z)
              + ')'
             )

        # Measure angle for three point
        print("*** Measure angle for three point.")
        constructionPoint = rootComp.originConstructionPoint
        vertex = brepBody.vertices.item(0)
        measureResult = app.measureManager.measureAngle(constructionPoint, point2, vertex)
        angle = measureResult.value
        print('Angle value is ' + str(angle))

        position1 = measureResult.positionOne
        position2 = measureResult.positionTwo
        position3 = measureResult.positionThree
        print('positionOne is ('
              + str(position1.x)
              + ','
              + str(position1.y)
              + ','
              + str(position1.z)
              + ')'
             )
        print('positionTwo is ('
              + str(position2.x)
              + ','
              + str(position2.y)
              + ','
              + str(position2.z)
              + ')'
             )
        print('positionThree is ('
              + str(position3.x)
              + ','
              + str(position3.y)
              + ','
              + str(position3.z)
              + ')'
             )

        # Measure angle for two object
        print("*** Measure angle for two objects.")
        brepFace = brepBody.faces.item(1)
        brepEdge = brepBody.edges.item(0)
        measureResult = app.measureManager.measureAngle(brepFace, brepEdge)
        angle = measureResult.value
        print('Angle value is ' + str(angle))

        # Get oriented bounding box
        print("*** Get oriented bounding box.")
        vector1 = adsk.core.Vector3D.create(0.0, 0.0, 1.0)
        vector2 = adsk.core.Vector3D.create(0.0, 1.0, 0.0)
        boundingBox = app.measureManager.getOrientedBoundingBox(brepBody, vector1, vector2)

        # Get the bounding box length, width and height
        length = boundingBox.length
        print("Bounding box length is " + str(length))
        width = boundingBox.width
        print("Bounding box width is " + str(width))
        height = boundingBox.height
        print("Bounding box height is " + str(height))

        # Get the bounding box width direction
        widthDirection = boundingBox.widthDirection
        heightDirection = boundingBox.heightDirection
        lengthDirection = boundingBox.lengthDirection
        print("Bounding box width direction is "
              + "("
              + str(widthDirection.x)
              + ", "
              + str(widthDirection.y)
              + ", "
              + str(widthDirection.z)
              + ")"
             )

        # Get the bounding contain a point or not
        pointA= adsk.core.Point3D.create(-2.0, 0.5, 2.0)
        isContain = boundingBox.contains(pointA)
        print("Dose the bounding box contain pointA? " + str(isContain))

        pointB = adsk.core.Point3D.create(0.0, 0.0, 0.0)
        isContain = boundingBox.contains(pointB)
        print("Dose the bounding box contain pointB? " + str(isContain))

        # Copy the bounding box
        boundingBoxCopy = boundingBox.copy()
        length = boundingBoxCopy.length
        print("The copied Bounding box length is " + str(length))

        # Set bounding box height
        boundingBoxCopy.height = 10.0
        length = boundingBoxCopy.height
        print("The new set length of the copied bounding box is " + str(length))

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/UserInterface/UserInterface.h>
#include <Core/Application/Document.h>
#include <Core/Application/Documents.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Construction/ConstructionPoint.h>
#include <Fusion/Sketch/SketchCurves.h>
#include <Fusion/Sketch/SketchLines.h>
#include <Fusion/Sketch/SketchLine.h>
#include <Core/Geometry/Point3D.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Core/Application/ValueInput.h>
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/BRep/BRepBody.h>
#include <Fusion/BRep/BRepEdges.h>
#include <Fusion/BRep/BRepEdge.h>
#include <Fusion/BRep/BRepVertices.h>
#include <Fusion/BRep/BRepVertex.h>
#include <Fusion/BRep/BRepFaces.h>
#include <Fusion/BRep/BRepFace.h>
#include <Core/Application/MeasureManager.h>
#include <Core/Application/MeasureResults.h>
#include <Core/Geometry/Vector3D.h>
#include <Core/Geometry/OrientedBoundingBox3D.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<Application> app;
Ptr<UserInterface> ui;

extern "C" XI_EXPORT bool run(const char* context)
{
    app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    // Create a new document
    Ptr<Documents> docs = app->documents();
    if (!docs)
        return false;

    Ptr<Document> doc = docs->add(DocumentTypes::FusionDesignDocumentType);
    if (!doc)
        return false;

    Ptr<Design> design = app->activeProduct();
    if (!design)
        return false;

    // Get the root component of active design
    Ptr<Component> rootComp = design->rootComponent();
    if (!rootComp)
        return false;

    // Create a new sketch on the yz plane
    Ptr<Sketches> sketches = rootComp->sketches();
    if (!sketches)
        return false;

    Ptr<ConstructionPlane> yzPlane = rootComp->yZConstructionPlane();
    if (!yzPlane)
        return false;

    Ptr<Sketch> sketch1 = sketches->add(yzPlane);
    if (!sketch1)
        return false;

    // Create sketch lines
    Ptr<SketchCurves> sketchCurves = sketch1->sketchCurves();
    if (!sketchCurves)
        return false;

    Ptr<SketchLines> sketchLines = sketchCurves->sketchLines();
    if (!sketchLines)
        return false;

    // Create sketch rectangle
    Ptr<Point3D> point1 = Point3D::create(0.0, 0.0, 0.0);
    Ptr<Point3D> point2 = Point3D::create(5.0, 5.0, 0.0);
    sketchLines->addTwoPointRectangle(point1, point2);

    // Get the profile
    Ptr<Profiles> profiles = sketch1->profiles();
    if (!profiles)
        return false;

    Ptr<Profile> profile = profiles->item(0);
    if (!profile)
        return false;

    // Create an extrusion input
    Ptr<Features> features = rootComp->features();
    if (!features)
        return false;

    Ptr<ExtrudeFeatures> extrudes = features->extrudeFeatures();
    if (!extrudes)
        return false;

    Ptr<ExtrudeFeatureInput> extrudeInput = extrudes->createInput(profile, FeatureOperations::NewBodyFeatureOperation);

    // Set extrude distance is 6 cm
    Ptr<ValueInput> distance = ValueInput::createByReal(6.0);
    // Set the distance extent
    extrudeInput->setDistanceExtent(false, distance);
    // Set the extrude type to be solid
    extrudeInput->isSolid(true);

    // Create the extrude
    Ptr<ExtrudeFeature> extrude = extrudes->add(extrudeInput);
    if (!extrude)
        return false;

    // Get the extrude brepbody
    Ptr<BRepBodies> brepBodies = extrude->bodies();
    if (!brepBodies)
        return false;

    Ptr<BRepBody> brepBody = brepBodies->item(0);
    if (!brepBody)
        return false;

    // Get one sketch line
    Ptr<SketchLine> sketchLine = sketchLines->item(0);
    if (!sketchLine)
        return false;

    // Get one brepEdge
    Ptr<BRepEdges> brepEdges = brepBody->edges();
    if (!brepEdges)
        return false;

    Ptr<BRepEdge> brepEdge = brepEdges->item(0);
    if (!brepEdge)
        return false;

    // Get measure manager
    Ptr<MeasureManager> measureMgr = app->measureManager();
    if (!measureMgr)
        return false;

    // Measure minimum distance
    Ptr<MeasureResults> results = measureMgr->measureMinimumDistance(sketchLine, brepEdge);
    if (!results)
        return false;

    double minIdstance = results->value();

    Ptr<Point3D> position1 = results->positionOne();
    if (!position1)
        return false;

    Ptr<Point3D> position2 = results->positionTwo();
    if (!position2)
        return false;

    // Get root component origin point
    Ptr<ConstructionPoint> constructionPoint = rootComp->originConstructionPoint();
    if (!constructionPoint)
        return false;

    // Get a brep Vertex
    Ptr<BRepVertices> brepVertices = brepBody->vertices();
    if (!brepVertices)
        return false;

    Ptr<BRepVertex> brepVertex = brepVertices->item(0);
    if (!brepVertex)
        return false;

    // Measure angle for three point
    results = measureMgr->measureAngle(constructionPoint, point2, brepVertex);
    if (!results)
        return false;

    double angle = results->value();

    position1 = results->positionOne();
    if (!position1)
        return false;

    position2 = results->positionTwo();
    if (!position2)
        return false;

    Ptr<Point3D> position3 = results->positionThree();
    if (!position3)
        return false;

    // Get a brep face
    Ptr<BRepFaces> brepFaces = brepBody->faces();
    if (!brepFaces)
        return false;

    Ptr<BRepFace> brepFace = brepFaces->item(1);
    if (!brepFace)
        return false;

    // Measure angle for two objects
    results = measureMgr->measureAngle(brepFace, brepEdge);
    if (!results)
        return false;

    angle = results->value();

    position1 = results->positionOne();
    if (!position1)
        return false;

    position2 = results->positionTwo();
    if (!position2)
        return false;

    position3 = results->positionThree();
    if (!position3)
        return false;

    // Get brep body's oriented bounding box
    Ptr<Vector3D> vector1 = Vector3D::create(0.0, 0.0, 1.0);
    Ptr<Vector3D> vector2 = Vector3D::create(0.0, 1.0, 0.0);

    Ptr<OrientedBoundingBox3D> boundingBox = measureMgr->getOrientedBoundingBox(brepBody, vector1, vector2);
    if (!boundingBox)
        return false;

    // Get the bounding box length, width and height
    double length = boundingBox->length();

    double width = boundingBox->width();

    double height = boundingBox->height();

    // Get the bounding box width direction
    Ptr<Vector3D> widthDir = boundingBox->widthDirection();
    if (!widthDir)
        return false;

    // Get the bounding box length direction
    Ptr<Vector3D> lengthDir = boundingBox->lengthDirection();
    if (!lengthDir)
        return false;

    // Get the bounding box height direction
    Ptr<Vector3D> heightDir = boundingBox->heightDirection();
    if (!heightDir)
        return false;

    // Get the bounding contain a point or not
    Ptr<Point3D> pointA = Point3D::create(-2.0, 0.5, 2.0);
    bool isContain = boundingBox->contains(pointA);

    Ptr<Point3D> pointB = Point3D::create(0.0, 0.0, 0.0);
    isContain = boundingBox->contains(pointB);

    // Copy the bounding box
    Ptr<OrientedBoundingBox3D> boudingBoxCopy = boundingBox->copy();
    if (!boudingBoxCopy)
        return false;

    // Set bounding box height
    boudingBoxCopy->height(10.0);
    double newHeight = boudingBoxCopy->height();

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |