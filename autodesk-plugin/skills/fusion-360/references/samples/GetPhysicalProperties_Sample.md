# Get Physical Properties API Sample

## Description

Script that demonstrates getting physical properties using the API. When this script is run it will create a new document, build a simple model, and get the various physical properties from the model.

## Code Samples

* [Python](#Python)
* [C++](#C++)

|  |
| --- |
| Copy Code |

```
#Author-
#Description-
import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Create a document.
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create sub occurrence
        occurrences = rootComp.occurrences
        subOcc = occurrences.addNewComponent(adsk.core.Matrix3D.create())

        # Get features from sub component
        subComponent = subOcc.component
        features = subComponent.features

        # Create sketch circle on the xz plane.
        sketches = subComponent.sketches
        sketch = sketches.add(subComponent.xZConstructionPlane)
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        sketchCircles.addByCenterRadius(centerPoint, 10)

        # Create a collection of entities for extrude
        entities0 = adsk.core.ObjectCollection.create()
        entities0.add(sketch.profiles.item(0))

        # Create a cylinder with ExtrudeFeature using the profile above.
        extrudeFeats = features.extrudeFeatures
        extrudeFeatureInput = extrudeFeats.createInput(entities0, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extrudeFeatureInput.isSolid = True
        extrudeFeatureInput.setDistanceExtent(False, adsk.core.ValueInput.createByReal(2.5))
        extrudeFeature = extrudeFeats.add(extrudeFeatureInput)

        # Get physical properties from body
        body = extrudeFeature.bodies[0]
        physicalProperties = body.physicalProperties

        # Get physical properties from occurrence
        physicalProperties = subOcc.physicalProperties

        # Get physical properties from occurrence (low accuracy)
        physicalProperties = subOcc.getPhysicalProperties(adsk.fusion.CalculationAccuracy.LowCalculationAccuracy);

	    # Get physical properties from occurrence (medium accuracy)
        physicalProperties = subOcc.getPhysicalProperties(adsk.fusion.CalculationAccuracy.MediumCalculationAccuracy);

	    # Get physical properties from occurrence (high accuracy)
        physicalProperties = subOcc.getPhysicalProperties(adsk.fusion.CalculationAccuracy.HighCalculationAccuracy);

        # Get physical properties from occurrence (very high accuracy)
        physicalProperties = subOcc.getPhysicalProperties(adsk.fusion.CalculationAccuracy.VeryHighCalculationAccuracy);

        # Get physical properties from component
        physicalProperties = subComponent.physicalProperties

        # Get physical properties from component (low accuracy)
        physicalProperties = subComponent.getPhysicalProperties(adsk.fusion.CalculationAccuracy.LowCalculationAccuracy);

	    # Get physical properties from component (medium accuracy)
        physicalProperties = subComponent.getPhysicalProperties(adsk.fusion.CalculationAccuracy.MediumCalculationAccuracy);

	    # Get physical properties from component (high accuracy)
        physicalProperties = subComponent.getPhysicalProperties(adsk.fusion.CalculationAccuracy.HighCalculationAccuracy);

        # Get physical properties from component (very high accuracy)
        physicalProperties = subComponent.getPhysicalProperties(adsk.fusion.CalculationAccuracy.VeryHighCalculationAccuracy);

        # Get data from physical properties
        area = physicalProperties.area
        density = physicalProperties.density
        mass = physicalProperties.mass
        volume = physicalProperties.volume

        # Get accuracy from physical properties
        accuracy = physicalProperties.accuracy

        # Get center of mass from physical properties
        cog = physicalProperties.centerOfMass

        # Get principal axes from physical properties
        (retVal, xAxis0, yAxis0, zAxis0) = physicalProperties.getPrincipalAxes()

        # Get the moments of inertia about the principal axes. Unit for returned values is kg/cm^2.
        (retVal,i1,i2,i3) = physicalProperties.getPrincipalMomentsOfInertia()

        # Get the radius of gyration about the principal axes. Unit for returned values is cm.
        (retVal, kx, ky, kz) = physicalProperties.getRadiusOfGyration()

        # Get the rotation from the world coordinate system of the target to the principal coordinate system.
        (retVal, rx, ry, rz) = physicalProperties.getRotationToPrincipal()

        # Get the moment of inertia about the world coordinate system.
        (retVal, xx, yy, zz, xy, yz, xz) = physicalProperties.getXYZMomentsOfInertia()

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
#include <Core/Application/ObjectCollection.h>
#include <Core/Application/ValueInput.h>
#include <Core/Geometry/Point3D.h>
#include <Core/Geometry/Matrix3D.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Fusion/PhysicalProperties.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Components/Occurrence.h>
#include <Fusion/Components/Occurrences.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/BRep/BRepBody.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchCurves.h>
#include <Fusion/Sketch/SketchCircles.h>
#include <Fusion/Sketch/SketchPoint.h>
#include <Fusion/Sketch/SketchPoints.h>

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

    // Create sub occurrence
    Ptr<Occurrences> occurrences = rootComp->occurrences();
    if (!occurrences)
        return false;
    Ptr<Occurrence> subOcc = occurrences->addNewComponent(Matrix3D::create());
    if (!subOcc)
        return false;

    // Get features from sub component
    Ptr<Component> subComponent = subOcc->component();
    if (!subComponent)
        return false;
    Ptr<Features> features = subComponent->features();
    if (!features)
        return false;

    // Create sketch circle on the xz plane.
    Ptr<Sketches> sketches = subComponent->sketches();
    if (!sketches)
        return false;
    Ptr<Sketch> sketch = sketches->add(subComponent->xZConstructionPlane());
    if (!sketch)
        return false;
    Ptr<SketchCurves> sketchCurves = sketch->sketchCurves();
    if (!sketchCurves)
        return false;
    Ptr<SketchCircles> sketchCirles = sketchCurves->sketchCircles();
    if (!sketchCirles)
        return false;
    Ptr<Point3D> centerPoint = Point3D::create(0, 0, 0);
    if (!centerPoint)
        return false;
    Ptr<SketchCircle> sketchCircle = sketchCirles->addByCenterRadius(centerPoint, 10);
    if (!sketchCircle)
        return false;

    // Create a collection of entities for extrude
    Ptr<ObjectCollection> entities0 = ObjectCollection::create();
    if (!entities0)
        return false;
    Ptr<Profiles> sketchProfiles = sketch->profiles();
    if (!sketchProfiles)
        return false;
    Ptr<Profile> sketchProfile = sketchProfiles->item(0);
    if (!sketchProfile)
        return false;
    entities0->add(sketchProfile);

    // Create a cylinder with ExtrudeFeature using the profile above.
    Ptr<ExtrudeFeatures> extrudeFeats = features->extrudeFeatures();
    if (!extrudeFeats)
        return false;
    Ptr<ExtrudeFeatureInput> extrudeFeatureInput =
        extrudeFeats->createInput(entities0, adsk::fusion::FeatureOperations::NewBodyFeatureOperation);
    if (!extrudeFeatureInput)
        return false;
    Ptr<ValueInput> distance = adsk::core::ValueInput::createByReal(2.0);
    if (!distance)
        return false;
    extrudeFeatureInput->isSolid(true);
    extrudeFeatureInput->setDistanceExtent(false, distance);
    Ptr<ExtrudeFeature> extrudeFeature = extrudeFeats->add(extrudeFeatureInput);
    if (!extrudeFeature)
        return false;

    // Get physical properties from body
    Ptr<BRepBodies> bodies = extrudeFeature->bodies();
    if (!bodies)
        return false;
    Ptr<BRepBody> body = bodies->item(0);
    Ptr<PhysicalProperties> physicalProperties = body->physicalProperties();

    // Get physical properties from occurrence
    physicalProperties = subOcc->physicalProperties();

    // Get physical properties from occurrence (low accuracy)
    physicalProperties = subOcc->getPhysicalProperties(LowCalculationAccuracy);

    // Get physical properties from occurrence (medium accuracy)
    physicalProperties = subOcc->getPhysicalProperties(MediumCalculationAccuracy);

    // Get physical properties from occurrence (high accuracy)
    physicalProperties = subOcc->getPhysicalProperties(HighCalculationAccuracy);

    // Get physical properties from occurrence (very high accuracy)
    physicalProperties = subOcc->getPhysicalProperties(VeryHighCalculationAccuracy);

    // Get physical properties from component
    physicalProperties = subComponent->physicalProperties();

    // Get physical properties from component (low accuracy)
    physicalProperties = subComponent->getPhysicalProperties(CalculationAccuracy::LowCalculationAccuracy);

    // Get physical properties from component (medium accuracy)
    physicalProperties = subComponent->getPhysicalProperties(CalculationAccuracy::MediumCalculationAccuracy);

    // Get physical properties from component (high accuracy)
    physicalProperties = subComponent->getPhysicalProperties(CalculationAccuracy::HighCalculationAccuracy);

    // Get physical properties from component (very high accuracy)
    physicalProperties = subComponent->getPhysicalProperties(CalculationAccuracy::VeryHighCalculationAccuracy);
    if (!physicalProperties)
        return false;

    // Get data from physical properties
    double area = physicalProperties->area();
    double density = physicalProperties->density();
    double mass = physicalProperties->mass();
    double volume = physicalProperties->volume();

    // Get accuracy from physical properties
    CalculationAccuracy accuracy = physicalProperties->accuracy();

    // Get center of mass from physical properties
    Ptr<Point3D> cog = physicalProperties->centerOfMass();

    // Get principal axes from physical properties
    Ptr<Vector3D> xAxis;
    Ptr<Vector3D> yAxis;
    Ptr<Vector3D> zAxis;
    physicalProperties->getPrincipalAxes(xAxis, yAxis, zAxis);

    // Get the moments of inertia about the principal axes. Unit for returned values is kg/cm^2.
    double i1 = 0, i2 = 0, i3 = 0;
    physicalProperties->getPrincipalMomentsOfInertia(i1, i2, i3);

    // Get the radius of gyration about the principal axes. Unit for returned values is cm.
    double kx = 0, ky = 0, kz = 0;
    physicalProperties->getRadiusOfGyration(kx, ky, kz);

    // Get the rotation from the world coordinate system of the target to the principal coordinate system.
    double rx = 0, ry = 0, rz = 0;
    physicalProperties->getRotationToPrincipal(rx, ry, rz);

    // Get the moment of inertia about the world coordinate system.
    double xx = 0, yy = 0, zz = 0, xy = 0, yz = 0, xz = 0;
    physicalProperties->getXYZMomentsOfInertia(xx, yy, zz, xy, yz, xz);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |