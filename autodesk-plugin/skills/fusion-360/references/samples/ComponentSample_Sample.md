# Component Sample

## Description

Component related functions

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

        allOccs = rootComp.occurrences
        transform = adsk.core.Matrix3D.create()

        # Create a component under root component
        occ1 = allOccs.addNewComponent(transform)
        subComp1 = occ1.component
        print(subComp1.revisionId)

        # Create a sketch in sub component 1
        sketches1 = subComp1.sketches
        sketch1 = sketches1.add(rootComp.yZConstructionPlane)
        print(subComp1.revisionId)

        # Get sketch lines
        sketchLines = sketch1.sketchCurves.sketchLines

        # Create sketch rectangle
        startPoint = adsk.core.Point3D.create(-8.0, 0, 0)
        endPoint = adsk.core.Point3D.create(8.0, 8.0, 0)
        sketchLines.addTwoPointRectangle(startPoint, endPoint)
        print(subComp1.revisionId)

        # Get the profile of the first sketch
        prof1 = sketch1.profiles.item(0)

        # Create an extrusion input
        extrudes1 = subComp1.features.extrudeFeatures
        extInput1 = extrudes1.createInput(prof1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Define that the extent is a distance extent of 2 cm
        distance1 = adsk.core.ValueInput.createByReal(2.0)
        # Set the distance extent
        extInput1.setDistanceExtent(False, distance1)
        # Set the extrude type to be solid
        extInput1.isSolid = True

        # Create the extrusion
        ext1 = extrudes1.add(extInput1)
        print(subComp1.revisionId)

        # Create a second occurrence
        transform2 = transform = adsk.core.Matrix3D.create()
        translation = adsk.core.Vector3D.create(10, 0, 0)
        transform2.translation = translation
        occ2 = allOccs.addExistingComponent(subComp1,transform2)

        # Ground to parent
        occ1.isGroundToParent = False
        occ2.isGroundToParent = True

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
#include <Core/Geometry/Point3D.h>
#include <Core/Geometry/Vector3D.h>
#include <Core/UserInterface/UserInterface.h>
#include <Core/Application/ObjectCollection.h>
#include <Core/Geometry/Matrix3D.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchCurves.h>
#include <Fusion/Sketch/SketchCurve.h>
#include <Fusion/Sketch/SketchPoints.h>
#include <Fusion/Sketch/SketchPoint.h>
#include <Fusion/Sketch/SketchLines.h>
#include <Fusion/Sketch/SketchLine.h>
#include <Fusion/Sketch/SketchFittedSplines.h>
#include <Fusion/Sketch/SketchFittedSpline.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Components/Occurrence.h>
#include <Fusion/Components/Occurrences.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionPlane.h>

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

    // Create a sub component under root component
    Ptr<Occurrences> occs = rootComp->occurrences();
    if (!occs)
        return false;

    Ptr<Matrix3D> transform = adsk::core::Matrix3D::create();
    if (!transform)
        return false;

    Ptr<Occurrence> subOcc1 = occs->addNewComponent(transform);
    if (!subOcc1)
        return false;

    Ptr<Component> subComp1 = subOcc1->component();
    if (!subComp1)
        return false;

    std::string revisionId1 = subComp1->revisionId();

    // Create sketch 1 in sub component 1
    Ptr<Sketches> sketches1 = subComp1->sketches();
    if (!sketches1)
        return false;

    Ptr<ConstructionPlane> yzPlane = rootComp->yZConstructionPlane();
    if (!yzPlane)
        return false;

    Ptr<Sketch> sketch1 = sketches1->add(yzPlane);
    if (!sketch1)
        return false;

    // Get sketch curves
    Ptr<SketchCurves> sketchCurves = sketch1->sketchCurves();
    if (!sketchCurves)
        return false;

    // Get sketch lines
    Ptr<SketchLines> sketchLines = sketchCurves->sketchLines();
    if (!sketchLines)
        return false;

    // Create sketch rectangle
    Ptr<Point3D> startPoint = Point3D::create(-8.0, 0, 0);

    Ptr<Point3D> endPoint = Point3D::create(8.0, 8.0, 0);
    sketchLines->addTwoPointRectangle(startPoint, endPoint);

    // Get the profile
    Ptr<Profiles> profs1 = sketch1->profiles();
    if (!profs1)
        return false;

    Ptr<Profile> prof1 = profs1->item(0);

    // Create an extrusion input
    Ptr<Features> feats1 = subComp1->features();
    if (!feats1)
        return false;

    Ptr<ExtrudeFeatures> extrudes1 = feats1->extrudeFeatures();
    if (!extrudes1)
        return false;

    Ptr<ExtrudeFeatureInput> extInput1 = extrudes1->createInput(prof1, FeatureOperations::NewBodyFeatureOperation);

    // Define that the extent is a distance extent of 2 cm
    Ptr<ValueInput> distance1 = ValueInput::createByReal(2.0);
    // Set the distance extent
    extInput1->setDistanceExtent(false, distance1);
    // Set the extrude type to be solid
    extInput1->isSolid(true);

    // Create the extrusion
    Ptr<ExtrudeFeature> ext1 = extrudes1->add(extInput1);
    if (!ext1)
        return false;

    std::string revisionId2 = subComp1->revisionId();

    // Create a transform for second sub component
    Ptr<Vector3D> translation = adsk::core::Vector3D::create(10, 0, 0);
    if (!translation)
        return false;

    Ptr<Matrix3D> transform2 = adsk::core::Matrix3D::create();
    if (!transform2)
        return false;

    transform2->translation(translation);

    // Create the second sub component
    Ptr<Occurrence> subOcc2 = occs->addExistingComponent(subComp1, transform2);
    if (!subOcc2)
        return false;

    // Ground to parent
    subOcc1->isGroundToParent(false);
    subOcc2->isGroundToParent(true);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |