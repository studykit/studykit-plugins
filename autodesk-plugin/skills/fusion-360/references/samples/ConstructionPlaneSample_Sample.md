# Construction Plane API Sample

## Description

Demonstrates creating construction plane by different ways.

## Code Samples

* [Python](#Python)
* [C++](#C++)

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        # Create a document.
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the root component of the active design
        rootComp = design.rootComponent

        # Create sketch
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xZConstructionPlane)

        # Create sketch circle
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        sketchCircles.addByCenterRadius(centerPoint, 5.0)

        # Get the profile defined by the circle
        prof = sketch.profiles.item(0)

        # Create an extrusion input
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Define that the extent is a distance extent of 5 cm
        distance = adsk.core.ValueInput.createByReal(5)
        # Set the distance extent to be symmetric
        extInput.setDistanceExtent(True, distance)
        # Set the extrude to be a solid one
        extInput.isSolid = True

        # Create an cylinder
        extrude = extrudes.add(extInput)

        # Create sketch line
        sketchLines = sketch.sketchCurves.sketchLines
        startPoint = adsk.core.Point3D.create(5, 5, 0)
        endPoint = adsk.core.Point3D.create(5, 10, 0)
        sketchLineOne = sketchLines.addByTwoPoints(startPoint, endPoint)
        endPointTwo = adsk.core.Point3D.create(10, 5, 0)
        sketchLineTwo = sketchLines.addByTwoPoints(startPoint, endPointTwo)

        # Create three sketch points
        sketchPoints = sketch.sketchPoints
        positionOne = adsk.core.Point3D.create(0, 5.0, 0)
        sketchPointOne = sketchPoints.add(positionOne)
        positionTwo = adsk.core.Point3D.create(5.0, 0, 0)
        sketchPointTwo = sketchPoints.add(positionTwo)
        positionThree = adsk.core.Point3D.create(0, -5.0, 0)
        sketchPointThree = sketchPoints.add(positionThree)

        # Get the profile again since the sketch has been edit.
        prof = sketch.profiles.item(0)

        # Get construction planes
        planes = rootComp.constructionPlanes

        # Create construction plane input
        planeInput = planes.createInput()

        # Add construction plane by offset
        offsetValue = adsk.core.ValueInput.createByReal(3.0)
        planeInput.setByOffset(prof, offsetValue)
        planeOne = planes.add(planeInput)

        # Get the health state of the plane
        health = planeOne.healthState
        if health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState or health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState:
            message = planeOne.errorOrWarningMessage

        # Add construction plane by angle
        angle = adsk.core.ValueInput.createByString('30.0 deg')
        planeInput.setByAngle(sketchLineOne, angle, prof)
        planes.add(planeInput)

        # Add construction plane by two planes
        planeInput.setByTwoPlanes(prof, planeOne)
        planes.add(planeInput)

        # Add construction plane by tangent
        cylinderFace = extrude.sideFaces.item(0)
        planeInput.setByTangent(cylinderFace, angle, rootComp.xYConstructionPlane)
        planes.add(planeInput)

        # Add construction plane by two edges
        planeInput.setByTwoEdges(sketchLineOne, sketchLineTwo)
        planes.add(planeInput)

        # Add construction plane by three points
        planeInput.setByThreePoints(sketchPointOne, sketchPointTwo, sketchPointThree)
        planes.add(planeInput)

        # Add construction plane by tangent at point
        planeInput.setByTangentAtPoint(cylinderFace, sketchPointOne)
        planes.add(planeInput)

        # Add construction plane by distance on path
        distance = adsk.core.ValueInput.createByReal(1.0)
        planeInput.setByDistanceOnPath(sketchLineOne, distance)
        planes.add(planeInput)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/Application/Document.h>
#include <Core/Application/Documents.h>
#include <Core/Application/ValueInput.h>
#include <Core/Geometry/Point3D.h>
#include <Core/Geometry/Vector3D.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Construction/ConstructionPlanes.h>
#include <Fusion/Construction/ConstructionPlaneInput.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchPoints.h>
#include <Fusion/Sketch/SketchPoint.h>
#include <Fusion/Sketch/SketchCurves.h>
#include <Fusion/Sketch/SketchCircles.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Sketch/SketchLines.h>
#include <Fusion/Sketch/SketchLine.h>
#include <Fusion/Sketch/SketchPoints.h>
#include <Fusion/Sketch/SketchPoint.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/BRep/BRepFaces.h>
#include <Fusion/BRep/BRepFace.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<UserInterface> ui;

extern "C" XI_EXPORT bool run(const char* context)
{
    Ptr<Application> app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    Ptr<Documents> docs = app->documents();
    if (!docs)
        return false;

    // Create a document.
    Ptr<Document> doc = docs->add(DocumentTypes::FusionDesignDocumentType);
    if (!doc)
        return false;

    Ptr<Design> design = app->activeProduct();
    if (!design)
        return false;

    // Get the root component of the active design
    Ptr<Component> rootComp = design->rootComponent();
    if (!rootComp)
        return false;

    // Create sketch
    Ptr<Sketches> sketches = rootComp->sketches();
    if (!sketches)
        return false;

    Ptr<Sketch> sketch = sketches->add(rootComp->xYConstructionPlane());
    if (!sketch)
        return false;

    // Create sketch circle
    Ptr<SketchCurves> curves = sketch->sketchCurves();
    if (!curves)
        return false;

    Ptr<SketchCircles> circles = curves->sketchCircles();
    if (!circles)
        return false;
    Ptr<Point3D> centerPoint = Point3D::create(0, 0, 0);
    circles->addByCenterRadius(centerPoint, 5.0);

    // Get the profile defined by the circle
    Ptr<Profiles> profs = sketch->profiles();
    if (!profs)
        return false;
    Ptr<Profile> prof = profs->item(0);

    // Create an extrusion input
    Ptr<Features> features = rootComp->features();
    if (!features)
        return false;

    Ptr<ExtrudeFeatures> extrudes = features->extrudeFeatures();
    if (!extrudes)
        return false;
    Ptr<ExtrudeFeatureInput> extInput = extrudes->createInput(prof, FeatureOperations::NewBodyFeatureOperation);

    // Define that the extent is a distance extent of 5 cm
    Ptr<ValueInput> distance = ValueInput::createByReal(5.0);

    // Set the distance extent to be symmetric
    extInput->setDistanceExtent(true, distance);

    // Set the extrude to be a solid one
    extInput->isSolid(true);

    // Create an cylinder
    Ptr<ExtrudeFeature> extrude = extrudes->add(extInput);
    if (!extrude)
        return false;

    // Create sketch line
    Ptr<SketchLines> sketchLines = curves->sketchLines();
    if (!sketchLines)
        return false;
    Ptr<Point3D> startPoint = Point3D::create(5.0, 5.0, 0);
    Ptr<Point3D> endPoint = Point3D::create(5.0, 10.0, 0);
    Ptr<SketchLine> sketchLineOne = sketchLines->addByTwoPoints(startPoint, endPoint);
    Ptr<Point3D> endPointTwo = Point3D::create(10.0, 5.0, 0);
    Ptr<SketchLine> sketchLineTwo = sketchLines->addByTwoPoints(startPoint, endPointTwo);

    // Create three sketch points
    Ptr<SketchPoints> sketchPoints = sketch->sketchPoints();
    if (!sketchPoints)
        return false;
    Ptr<Point3D> positionOne = Point3D::create(0, 5.0, 0);
    Ptr<SketchPoint> sketchPointOne = sketchPoints->add(positionOne);
    Ptr<Point3D> positionTwo = Point3D::create(5.0, 0, 0);
    Ptr<SketchPoint> sketchPointTwo = sketchPoints->add(positionTwo);
    Ptr<Point3D> positionThree = Point3D::create(0, -5.0, 0);
    Ptr<SketchPoint> sketchPointThree = sketchPoints->add(positionThree);

    prof = profs->item(0);

    // Get construction planes
    Ptr<ConstructionPlanes> planes = rootComp->constructionPlanes();
    if (!planes)
        return false;

    // Create construction plane input
    Ptr<ConstructionPlaneInput> planeInput = planes->createInput();
    if (!planeInput)
        return false;

    // Add construction plane by offset
    Ptr<ValueInput> offsetValue = ValueInput::createByReal(3.0);
    planeInput->setByOffset(prof, offsetValue);
    Ptr<ConstructionPlane> planeOne = planes->add(planeInput);

    // Get the health state of a construction plane
    adsk::fusion::FeatureHealthStates health = planeOne->healthState();
    if (health == adsk::fusion::FeatureHealthStates::ErrorFeatureHealthState ||
        health == adsk::fusion::FeatureHealthStates::WarningFeatureHealthState)
    {
        std::string msg = planeOne->errorOrWarningMessage();
    }

    // Add construction plane by angle
    Ptr<ValueInput> angle = ValueInput::createByString("30.0 deg");
    planeInput->setByAngle(sketchLineOne, angle, prof);
    planes->add(planeInput);

    // Add construction plane by two planes
    planeInput->setByTwoPlanes(prof, planeOne);
    planes->add(planeInput);

    // Add construction plane by tangent
    Ptr<BRepFaces> extSideFaces = extrude->sideFaces();
    if (!extSideFaces)
        return false;
    Ptr<BRepFace> cylinderFace = extSideFaces->item(0);
    planeInput->setByTangent(cylinderFace, angle, rootComp->xZConstructionPlane());
    planes->add(planeInput);

    // Add construction plane by two edges
    planeInput->setByTwoEdges(sketchLineOne, sketchLineTwo);
    planes->add(planeInput);

    // Add construction plane by three points
    planeInput->setByThreePoints(sketchPointOne, sketchPointTwo, sketchPointThree);
    planes->add(planeInput);

    // Add construction plane by tangent at point
    planeInput->setByTangentAtPoint(cylinderFace, sketchPointOne);
    planes->add(planeInput);

    // Add construction plane by distance on path
    distance = ValueInput::createByReal(1.0);
    planeInput->setByDistanceOnPath(sketchLineOne, distance);
    planes->add(planeInput);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |