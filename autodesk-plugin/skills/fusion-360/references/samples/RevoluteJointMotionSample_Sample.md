# RevoluteJointMotion API Sample

## Description

Demonstrates creating a joint with revolute joint motion.

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
        ui = app.userInterface

        # Create a document.
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the root component of the active design
        rootComp = design.rootComponent

        # Create sketch in root component
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xZConstructionPlane)
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint0 = adsk.core.Point3D.create(0, 0, 0)
        circle0 = sketchCircles.addByCenterRadius(centerPoint0, 5.0)
        centerPoint1 = adsk.core.Point3D.create(10, 10, 0)
        circle1 = sketchCircles.addByCenterRadius(centerPoint1, 5.0)

        # Get the profile defined by the circle
        prof0 = sketch.profiles.item(0)
        prof1 = sketch.profiles.item(1)

        # Create an extrusion input and make sure it's in a new component
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof0, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)

        # Set the extrusion input
        distance = adsk.core.ValueInput.createByReal(5)
        extInput.setDistanceExtent(True, distance)
        extInput.isSolid = True

        # Create the extrusion
        ext = extrudes.add(extInput)

        # Get the side face of the created extrusion body
        sideFace = ext.sideFaces.item(0)

        # Create the first joint geometry with the side face
        geo0 = adsk.fusion.JointGeometry.createByNonPlanarFace(sideFace, adsk.fusion.JointKeyPointTypes.StartKeyPoint)

        # Create the second joint geometry with prof1
        geo1 = adsk.fusion.JointGeometry.createByProfile(prof1, circle1, adsk.fusion.JointKeyPointTypes.CenterKeyPoint)

        # Create joint input
        joints = rootComp.joints
        jointInput = joints.createInput(geo0, geo1)

        # Set the joint input
        angle = adsk.core.ValueInput.createByString('90 deg')
        jointInput.angle = angle
        offset = adsk.core.ValueInput.createByString('1 cm')
        jointInput.offset = offset
        jointInput.isFlipped = True
        jointInput.setAsRevoluteJointMotion(adsk.fusion.JointDirections.YAxisJointDirection)

        # Create the joint
        joint = joints.add(jointInput)

        revoluteMotion = joint.jointMotion
        limits = revoluteMotion.rotationLimits
        limits.isMinimumValueEnabled = True
        limits.minimumValue = 3.14 / 3
        limits.isMaximumValueEnabled = True
        limits.maximumValue = 3.14 / 3 * 2
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
#include <Core/Geometry/Point3D.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/BRep/BRepFace.h>
#include <Fusion/BRep/BRepFaces.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Components/Joint.h>
#include <Fusion/Components/JointGeometry.h>
#include <Fusion/Components/JointInput.h>
#include <Fusion/Components/JointLimits.h>
#include <Fusion/Components/Joints.h>
#include <Fusion/Components/RevoluteJointMotion.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Sketch/SketchCircles.h>
#include <Fusion/Sketch/SketchCurves.h>

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

    // Create sketch in root component
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
    Ptr<Point3D> centerPoint0 = Point3D::create(0, 0, 0);
    if (!centerPoint0)
        return false;
    Ptr<SketchCircle> circle0 = sketchCircles->addByCenterRadius(centerPoint0, 5.0);
    if (!circle0)
        return false;
    Ptr<Point3D> centerPoint1 = Point3D::create(10, 10, 0);
    if (!centerPoint1)
        return false;
    Ptr<SketchCircle> circle1 = sketchCircles->addByCenterRadius(centerPoint1, 5.0);
    if (!circle1)
        return false;

    // Get the profile defined by the circle
    Ptr<Profiles> profs = sketch->profiles();
    if (!profs)
        return false;
    Ptr<Profile> prof0 = profs->item(0);
    if (!prof0)
        return false;
    Ptr<Profile> prof1 = profs->item(1);
    if (!prof1)
        return false;

    // Create an extrusion input and make sure it's in a new component
    Ptr<Features> feats = rootComp->features();
    if (!feats)
        return false;
    Ptr<ExtrudeFeatures> extrudes = feats->extrudeFeatures();
    if (!extrudes)
        return false;
    Ptr<ExtrudeFeatureInput> extInput = extrudes->createInput(prof0, FeatureOperations::NewComponentFeatureOperation);
    if (!extInput)
        return false;

    // Set the extrusion input
    Ptr<ValueInput> distance = ValueInput::createByReal(5);
    if (!distance)
        return false;
    extInput->setDistanceExtent(true, distance);
    extInput->isSolid(true);

    // Create the extrusion
    Ptr<ExtrudeFeature> ext = extrudes->add(extInput);
    if (!ext)
        return false;

    // Get the side face of the created extrusion body
    Ptr<BRepFaces> sideFaces = ext->sideFaces();
    if (!sideFaces)
        return false;
    Ptr<BRepFace> sideFace = sideFaces->item(0);
    if (!sideFace)
        return false;

    // Create the first joint geometry with the side face
    Ptr<JointGeometry> geo0 = JointGeometry::createByNonPlanarFace(sideFace, JointKeyPointTypes::StartKeyPoint);
    if (!geo0)
        return false;

    // Create the second joint geometry with prof1
    Ptr<JointGeometry> geo1 = JointGeometry::createByProfile(prof1, circle1, JointKeyPointTypes::CenterKeyPoint);
    if (!geo1)
        return false;

    // Create joint input
    Ptr<Joints> joints = rootComp->joints();
    if (!joints)
        return false;
    Ptr<JointInput> jointInput = joints->createInput(geo0, geo1);
    if (!jointInput)
        return false;

    // Set the joint input
    Ptr<ValueInput> angle = ValueInput::createByString("90 deg");
    if (!angle)
        return false;
    jointInput->angle(angle);
    Ptr<ValueInput> offset = ValueInput::createByString("1 cm");
    if (!offset)
        return false;
    jointInput->offset(offset);
    jointInput->isFlipped(true);
    jointInput->setAsRevoluteJointMotion(JointDirections::YAxisJointDirection);

    // Create the joint
    Ptr<Joint> joint = joints->add(jointInput);
    if (!joint)
        return false;

    Ptr<RevoluteJointMotion> revoluteMotion = joint->jointMotion();
    if (!revoluteMotion)
        return false;
    Ptr<JointLimits> limits = revoluteMotion->rotationLimits();
    if (!limits)
        return false;
    limits->isMinimumValueEnabled(true);
    limits->minimumValue(3.14 / 3);
    limits->isMaximumValueEnabled(true);
    limits->maximumValue(3.14 / 3 * 2);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |