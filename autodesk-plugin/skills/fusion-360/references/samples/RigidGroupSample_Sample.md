# Rigid Group API Sample

## Description

Demonstrates creating a new Rigid Group.

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

        # Create four sub components under root component
        allOccs = rootComp.occurrences

        transform0 = adsk.core.Matrix3D.create()
        vector3d0 = adsk.core.Vector3D.create(10.0, 0.0, 0.0)
        transform0.translation = vector3d0
        subOcc0 = allOccs.addNewComponent(transform0)

        transform1 = adsk.core.Matrix3D.create()
        vector3d1 = adsk.core.Vector3D.create(0.0, 0.0, 12.0)
        transform1.translation = vector3d1
        subOcc1 = allOccs.addNewComponent(transform1)

        transform2 = adsk.core.Matrix3D.create()
        vector3d2 = adsk.core.Vector3D.create(-8.0, 0.0, 0.0)
        transform2.translation = vector3d2
        subOcc2 = allOccs.addNewComponent(transform2)

        transform3 = adsk.core.Matrix3D.create()
        vector3d3 = adsk.core.Vector3D.create(0.0, 0.0, -6.0)
        transform3.translation = vector3d3
        subOcc3 = allOccs.addNewComponent(transform3)

        # Create cylinder 1 in sub component 1
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        subComp0 = subOcc0.component
        sketches0 = subComp0.sketches
        sketch0 = sketches0.add(subComp0.xZConstructionPlane)
        sketchCircles0 = sketch0.sketchCurves.sketchCircles
        sketchCircles0.addByCenterRadius(centerPoint, 0.5)

        profile0 = sketch0.profiles.item(0)
        extrudes0 = subComp0.features.extrudeFeatures
        extInput0 = extrudes0.createInput(profile0, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        distance0 = adsk.core.ValueInput.createByString("50 mm")
        extInput0.setDistanceExtent(False, distance0)
        extInput0.isSolid = False
        extrudes0.add(extInput0)

        # Create cylinder 2 in sub component 2
        subComp1 = subOcc1.component
        sketches1 = subComp1.sketches
        sketch1 = sketches1.add(subComp1.xZConstructionPlane)
        sketchCircles1 = sketch1.sketchCurves.sketchCircles
        sketchCircles1.addByCenterRadius(centerPoint, 0.75)

        profile1 = sketch1.profiles.item(0)
        extrudes1 = subComp1.features.extrudeFeatures
        extInput1 = extrudes1.createInput(profile1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        distance1 = adsk.core.ValueInput.createByString("75 mm")
        extInput1.setDistanceExtent(False, distance1)
        extInput1.isSolid = False
        extrudes1.add(extInput1)

        # Create cylinder 3 in sub component 3
        subComp2 = subOcc2.component
        sketches2 = subComp2.sketches
        sketch2 = sketches2.add(subComp2.xZConstructionPlane)
        sketchCircles2 = sketch2.sketchCurves.sketchCircles
        sketchCircles2.addByCenterRadius(centerPoint, 1.0)

        profile2 = sketch2.profiles.item(0)
        extrudes2 = subComp2.features.extrudeFeatures
        extInput2 = extrudes2.createInput(profile2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        distance2 = adsk.core.ValueInput.createByString("100 mm")
        extInput2.setDistanceExtent(False, distance2)
        extInput2.isSolid = False
        extrudes2.add(extInput2)

        # Create cylinder 4 in sub component 4
        subComp3 = subOcc3.component
        sketches3 = subComp3.sketches
        sketch3 = sketches3.add(subComp3.xZConstructionPlane)
        sketchCircles3 = sketch3.sketchCurves.sketchCircles
        sketchCircles3.addByCenterRadius(centerPoint, 1.25)

        profile3 = sketch3.profiles.item(0)
        extrudes3 = subComp3.features.extrudeFeatures
        extInput3 = extrudes3.createInput(profile3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        distance3 = adsk.core.ValueInput.createByString("125 mm")
        extInput3.setDistanceExtent(False, distance3)
        extInput3.isSolid = False
        extrudes3.add(extInput3)

        # Create object collection
        occs = adsk.core.ObjectCollection.create()
        occs.add(subOcc0)
        occs.add(subOcc1)
        occs.add(subOcc2)
        occs.add(subOcc3)

        # Create a Rigid group
        isIncludeChildren = True
        rigidGroups_ = rootComp.rigidGroups
        rigidGroups_.add(occs, isIncludeChildren)

        camera_ = app.activeViewport.camera
        camera_.isFitView = True
        app.activeViewport.camera = camera_

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
#include <Core/Application/Product.h>
#include <Core/Application/ValueInput.h>
#include <Core/Application/Viewport.h>
#include <Core/Application/Camera.h>
#include <Core/Application/ObjectCollection.h>
#include <Core/Geometry/Point3D.h>
#include <Core/Geometry/Matrix3D.h>
#include <Core/Geometry/Vector3D.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Construction/ConstructionPlanes.h>
#include <Fusion/Construction/ConstructionPlaneInput.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Components/RigidGroups.h>
#include <Fusion/Components/RigidGroup.h>
#include <Fusion/Components/Occurrence.h>
#include <Fusion/Components/Occurrences.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Sketch/SketchCircles.h>
#include <Fusion/Sketch/SketchCurves.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<Application> app;
Ptr<UserInterface> ui;

bool CreateCylinder(Ptr<Occurrence> occ, double diameter, double height, bool isSolid)
{
    Ptr<Component> comp = occ->component();
    if (!comp)
        return false;
    Ptr<Sketches> sketches = comp->sketches();
    if (!sketches)
        return false;
    Ptr<ConstructionPlane> xzPlane = comp->xZConstructionPlane();
    if (!xzPlane)
        return false;
    Ptr<Sketch> sketch = sketches->add(xzPlane);
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
    Ptr<SketchCircle> sketchCircle = sketchCircles->addByCenterRadius(centerPoint, diameter);
    if (!sketchCircle)
        return false;

    // Get the profile defined by the circle
    Ptr<Profiles> profs = sketch->profiles();
    if (!profs)
        return false;
    Ptr<Profile> profile = profs->item(0);
    if (!profile)
        return false;

    // Create an extrude input
    Ptr<Features> feats = comp->features();
    if (!feats)
        return false;
    Ptr<ExtrudeFeatures> extrudes = feats->extrudeFeatures();
    if (!extrudes)
        return false;
    Ptr<ExtrudeFeatureInput> extInput = extrudes->createInput(profile, FeatureOperations::NewBodyFeatureOperation);
    if (!extInput)
        return false;

    // Set the extrude input
    Ptr<ValueInput> distance = ValueInput::createByReal(height);
    if (!distance)
        return false;
    extInput->setDistanceExtent(false, distance);
    extInput->isSolid(isSolid);

    // Create the extrude
    Ptr<ExtrudeFeature> extrude = extrudes->add(extInput);
    if (!extrude)
        return false;

    return true;
}

extern "C" XI_EXPORT bool run(const char* context)
{
    app = Application::get();
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

    // Create four sub components under root component
    Ptr<Occurrences> occs = rootComp->occurrences();
    if (!occs)
        return false;

    // sub component 1
    Ptr<Matrix3D> transform0 = adsk::core::Matrix3D::create();
    if (!transform0)
        return false;
    Ptr<Vector3D> vector3d0 = adsk::core::Vector3D::create(10.0, 0.0, 0.0);
    if (!vector3d0)
        return false;
    transform0->translation(vector3d0);
    Ptr<Occurrence> subOcc0 = occs->addNewComponent(transform0);
    if (!subOcc0)
        return false;

    // sub component 2
    Ptr<Matrix3D> transform1 = adsk::core::Matrix3D::create();
    if (!transform1)
        return false;
    Ptr<Vector3D> vector3d1 = adsk::core::Vector3D::create(0.0, 0.0, 12.0);
    if (!vector3d1)
        return false;
    transform1->translation(vector3d1);
    Ptr<Occurrence> subOcc1 = occs->addNewComponent(transform1);
    if (!subOcc1)
        return false;

    // sub component 3
    Ptr<Matrix3D> transform2 = adsk::core::Matrix3D::create();
    if (!transform2)
        return false;
    Ptr<Vector3D> vector3d2 = adsk::core::Vector3D::create(-8.0, 0.0, 0.0);
    if (!vector3d2)
        return false;
    transform2->translation(vector3d2);
    Ptr<Occurrence> subOcc2 = occs->addNewComponent(transform2);
    if (!subOcc2)
        return false;

    // sub component 4
    Ptr<Matrix3D> transform3 = adsk::core::Matrix3D::create();
    if (!transform3)
        return false;
    Ptr<Vector3D> vector3d3 = adsk::core::Vector3D::create(0.0, 0.0, -6.0);
    if (!vector3d3)
        return false;
    transform3->translation(vector3d3);
    Ptr<Occurrence> subOcc3 = occs->addNewComponent(transform3);
    if (!subOcc3)
        return false;

    // Create an object collection of occurrences
    Ptr<ObjectCollection> occGroups = adsk::core::ObjectCollection::create();
    if (!occGroups)
        return false;
    occGroups->add(subOcc0);
    occGroups->add(subOcc1);
    occGroups->add(subOcc2);
    occGroups->add(subOcc3);

    // Create four cylinders in four sub components
    bool result0 = CreateCylinder(subOcc0, 0.5, 5, false);
    if (!result0)
        return false;

    bool result1 = CreateCylinder(subOcc1, 0.75, 7.5, false);
    if (!result1)
        return false;

    bool result2 = CreateCylinder(subOcc2, 1.0, 10, false);
    if (!result2)
        return false;

    bool result3 = CreateCylinder(subOcc3, 1.25, 12.5, false);
    if (!result3)
        return false;

    // Create a RigidGroup
    bool isIncludeChildren = true;
    Ptr<RigidGroups> rigidGroups_ = rootComp->rigidGroups();
    if (!rigidGroups_)
        return false;
    Ptr<RigidGroup> rigidGroup = rigidGroups_->add(occGroups, isIncludeChildren);
    if (!rigidGroup)
        return false;

    // Fit to window
    Ptr<Viewport> viewPort = app->activeViewport();
    if (!viewPort)
        return false;
    Ptr<Camera> cam = viewPort->camera();
    if (!cam)
        return false;
    cam->isFitView(true);
    viewPort->camera(cam);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |