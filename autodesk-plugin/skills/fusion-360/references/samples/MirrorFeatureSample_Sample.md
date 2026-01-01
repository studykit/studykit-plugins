# Mirror Feature API Sample

## Description

Demonstrates creating a new mirror feature

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
        sketchLines = sketch.sketchCurves.sketchLines
        startPoint = adsk.core.Point3D.create(0, 0, 0)
        endPoint = adsk.core.Point3D.create(5, 5, 0)
        sketchLines.addTwoPointRectangle(startPoint, endPoint)

        # Get the profile defined by the rectangle.
        prof = sketch.profiles.item(0)

        # Create an extrusion input.
        features = rootComp.features
        extrudes = features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Define that the extent is a distance extent of 5 cm.
        distance = adsk.core.ValueInput.createByReal(5)
        extInput.setDistanceExtent(False, distance)

        # Create the extrusion.
        ext = extrudes.add(extInput)

        # Get the body created by extrusion
        body = ext.bodies.item(0)

        # Get a face of the body
        face = body.faces.item(0)

        # Create a construction plane by offset
        planes = rootComp.constructionPlanes
        planeInput = planes.createInput()
        offsetDistance = adsk.core.ValueInput.createByString('5 cm')
        planeInput.setByOffset(face, offsetDistance)
        plane = planes.add(planeInput)

        # Create input entities for mirror feature
        inputEntites = adsk.core.ObjectCollection.create()
        inputEntites.add(body)

        # Create the input for mirror feature
        mirrorFeatures = features.mirrorFeatures
        mirrorInput = mirrorFeatures.createInput(inputEntites, plane)

        # Create the mirror feature
        mirrorFeature = mirrorFeatures.add(mirrorInput)
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
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Construction/ConstructionPlanes.h>
#include <Fusion/Construction/ConstructionPlaneInput.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/Features/MirrorFeature.h>
#include <Fusion/Features/MirrorFeatures.h>
#include <Fusion/Features/MirrorFeatureInput.h>
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
    Ptr<SketchLines> sketchLines = sketchCurves->sketchLines();
    if (!sketchLines)
        return false;
    Ptr<Point3D> startPoint = Point3D::create(0, 0, 0);
    if (!startPoint)
        return false;
    Ptr<Point3D> endPoint = Point3D::create(5, 5, 0);
    if (!endPoint)
        return false;
    sketchLines->addTwoPointRectangle(startPoint, endPoint);

    // Get the profile defined by the rectangle.
    Ptr<Profiles> profs = sketch->profiles();
    if (!profs)
        return false;
    Ptr<Profile> prof = profs->item(0);
    if (!prof)
        return false;

    // Create an extrusion input.
    Ptr<Features> features = rootComp->features();
    if (!features)
        return false;
    Ptr<ExtrudeFeatures> extrudes = features->extrudeFeatures();
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

    // Get a face of the body
    Ptr<BRepFaces> faces = body->faces();
    if (!faces)
        return false;
    Ptr<BRepFace> face = faces->item(0);
    if (!face)
        return false;

    // Create a construction plane by offset
    Ptr<ConstructionPlanes> planes = rootComp->constructionPlanes();
    if (!planes)
        return false;
    Ptr<ConstructionPlaneInput> planeInput = planes->createInput();
    if (!planeInput)
        return false;
    Ptr<ValueInput> offsetDistance = ValueInput::createByString("5 cm");
    if (!offsetDistance)
        return false;
    planeInput->setByOffset(face, offsetDistance);
    Ptr<ConstructionPlane> plane = planes->add(planeInput);
    if (!plane)
        return false;

    // Create input entities for mirror feature
    Ptr<ObjectCollection> inputEntites = ObjectCollection::create();
    if (!inputEntites)
        return false;
    inputEntites->add(body);

    // Create the input for mirror feature
    Ptr<MirrorFeatures> mirrorFeatures = features->mirrorFeatures();
    if (!mirrorFeatures)
        return false;
    Ptr<MirrorFeatureInput> mirrorInput = mirrorFeatures->createInput(inputEntites, plane);
    if (!mirrorInput)
        return false;

    // Create the mirror feature
    Ptr<MirrorFeature> mirrorFeature = mirrorFeatures->add(mirrorInput);
    if (!mirrorFeature)
        return false;

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |