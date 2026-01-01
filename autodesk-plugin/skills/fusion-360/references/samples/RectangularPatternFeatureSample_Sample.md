# RectangularPattern Feature

## Description

Demonstrates creating a new rectangular pattern feature.

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

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create sketch
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xZConstructionPlane)
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        sketchCircles.addByCenterRadius(centerPoint, 3.0)

        # Get the profile defined by the circle.
        prof = sketch.profiles.item(0)

        # Create an extrusion input
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Define that the extent is a distance extent of 5 cm.
        distance = adsk.core.ValueInput.createByReal(5)
        extInput.setDistanceExtent(False, distance)

        # Create the extrusion.
        ext = extrudes.add(extInput)

        # Get the body created by extrusion
        body = ext.bodies.item(0)

        # Create input entities for rectangular pattern
        inputEntites = adsk.core.ObjectCollection.create()
        inputEntites.add(body)

        # Get x and y axes for rectangular pattern
        xAxis = rootComp.xConstructionAxis
        yAxis = rootComp.yConstructionAxis

        # Quantity and distance
        quantityOne = adsk.core.ValueInput.createByString('3')
        distanceOne = adsk.core.ValueInput.createByString('8 cm')
        quantityTwo = adsk.core.ValueInput.createByString('3')
        distanceTwo = adsk.core.ValueInput.createByString('8 cm')

        # Create the input for rectangular pattern
        rectangularPatterns = rootComp.features.rectangularPatternFeatures
        rectangularPatternInput = rectangularPatterns.createInput(inputEntites, xAxis, quantityOne, distanceOne, adsk.fusion.PatternDistanceType.SpacingPatternDistanceType)

        # Set the data for second direction
        rectangularPatternInput.setDirectionTwo(yAxis, quantityTwo, distanceTwo)

        # Create the rectangular pattern
        rectangularFeature = rectangularPatterns.add(rectangularPatternInput)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/Application/Documents.h>
#include <Core/Application/Document.h>
#include <Core/Application/ObjectCollection.h>
#include <Core/Application/Product.h>
#include <Core/Application/ValueInput.h>
#include <Core/Geometry/Point3D.h>
#include <Core/Geometry/Line3D.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/BRep/BRepBody.h>
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/BRep/BRepFace.h>
#include <Fusion/BRep/BRepFaces.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionAxis.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/Features/RectangularPatternFeature.h>
#include <Fusion/Features/RectangularPatternFeatures.h>
#include <Fusion/Features/RectangularPatternFeatureInput.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Sketch/SketchCircles.h>
#include <Fusion/Sketch/SketchCurves.h>
#include <Fusion/Sketch/SketchLine.h>
#include <Fusion/Sketch/SketchLines.h>

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

    Ptr<Documents> documents = app->documents();
    if (!documents)
        return false;

    Ptr<Document> doc = documents->add(DocumentTypes::FusionDesignDocumentType);
    if (!doc)
        return false;

    Ptr<Product> product = app->activeProduct();
    if (!product)
        return false;

    Ptr<Design> design = product;
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
    Ptr<ConstructionPlane> xz = rootComp->xZConstructionPlane();
    if (!xz)
        return false;
    Ptr<Sketch> sketch = sketches->add(xz);
    if (!sketch)
        return false;
    Ptr<SketchCurves> sketchCurves = sketch->sketchCurves();
    if (!sketchCurves)
        return false;
    Ptr<SketchCircles> sketchCircles = sketchCurves->sketchCircles();
    if (!sketchCircles)
        return false;
    Ptr<Point3D> centerPoint = Point3D::create(0, 0, 0);
    if (!centerPoint)
        return false;
    Ptr<SketchCircle> circle = sketchCircles->addByCenterRadius(centerPoint, 3.0);
    if (!circle)
        return false;

    // Get the profile defined by the circle.
    Ptr<Profiles> profs = sketch->profiles();
    if (!profs)
        return false;
    Ptr<Profile> prof = profs->item(0);
    if (!prof)
        return false;

    // Create an extrusion input
    Ptr<Features> feats = rootComp->features();
    if (!feats)
        return false;
    Ptr<ExtrudeFeatures> extrudes = feats->extrudeFeatures();
    if (!extrudes)
        return false;
    Ptr<ExtrudeFeatureInput> extInput = extrudes->createInput(prof, FeatureOperations::NewBodyFeatureOperation);
    if (!extInput)
        return false;

    // Define that the extent is a distance extent of 5 cm.
    Ptr<ValueInput> distance = ValueInput::createByReal(5);
    if (!distance)
        return false;
    extInput->setDistanceExtent(false, distance);

    // Create the extrusion.
    Ptr<ExtrudeFeature> ext = extrudes->add(extInput);
    if (!ext)
        return false;

    // Get the body created by extrusion
    Ptr<BRepBodies> bodies = ext->bodies();
    if (!bodies)
        return false;
    Ptr<BRepBody> body = bodies->item(0);
    if (!body)
        return false;

    // Create input entities for rectangular pattern
    Ptr<ObjectCollection> inputEntites = ObjectCollection::create();
    if (!inputEntites)
        return false;
    inputEntites->add(body);

    // Get x and y axes for rectangular pattern
    Ptr<ConstructionAxis> xAxis = rootComp->xConstructionAxis();
    if (!xAxis)
        return false;
    Ptr<ConstructionAxis> yAxis = rootComp->yConstructionAxis();
    if (!yAxis)
        return false;

    // Quantity and distance
    Ptr<ValueInput> quantityOne = ValueInput::createByString("3");
    if (!quantityOne)
        return false;
    Ptr<ValueInput> distanceOne = ValueInput::createByString("8 cm");
    if (!distanceOne)
        return false;
    Ptr<ValueInput> quantityTwo = ValueInput::createByString("3");
    if (!quantityTwo)
        return false;
    Ptr<ValueInput> distanceTwo = ValueInput::createByString("8 cm");
    if (!distanceTwo)
        return false;

    // Create the input for rectangular pattern
    Ptr<RectangularPatternFeatures> rectangularPatterns = feats->rectangularPatternFeatures();
    if (!rectangularPatterns)
        return false;
    Ptr<RectangularPatternFeatureInput> rectangularPatternInput = rectangularPatterns->createInput(
        inputEntites, xAxis, quantityOne, distanceOne, PatternDistanceType::SpacingPatternDistanceType);
    if (!rectangularPatternInput)
        return false;

    // Set the data for second direction
    rectangularPatternInput->setDirectionTwo(yAxis, quantityTwo, distanceTwo);

    // Create the rectangular pattern
    Ptr<RectangularPatternFeature> rectangularFeature = rectangularPatterns->add(rectangularPatternInput);
    if (!rectangularFeature)
        return false;

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |