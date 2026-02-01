# Get Volume of Active Design API Sample

## Description

Traverses through the active design and totals the volume of every body within the design.

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

        design = app.activeProduct
        if not design:
            ui.messageBox('No active Fusion design', 'No Design')
            return

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Iterate over any bodies in the root component.
        totalVolume = 0
        for j in range(0, rootComp.bRepBodies.count):
            body = rootComp.bRepBodies.item(j)

            # Get the volume of the current body and add it to the total.
            totalVolume += body.volume

        # Iterate through all of the occurrences in the assembly.
        for i in range(0, rootComp.allOccurrences.count):
            occ = rootComp.allOccurrences.item(i)

            # Get the associated component.
            comp = occ.component

            # Iterate over all of the bodies within the component.
            for j in range(0, comp.bRepBodies.count):
                body = comp.bRepBodies.item(j)

                # Get the volume of the current body and add it to the total.
                totalVolume += body.volume

        # Format a string to display the volume using the default distance units.
        result = design.unitsManager.formatValue(totalVolume, design.unitsManager.defaultLengthUnits + '^3')
        ui.messageBox('The volume of the entire asembly is: ' + result)
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
#include <Core/Application/UnitsManager.h>
#include <Core/Application/ValueInput.h>
#include <Core/Geometry/Point3D.h>
#include <Core/Geometry/Line3D.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/BRep/BRepBody.h>
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Components/Occurrence.h>
#include <Fusion/Components/OccurrenceList.h>
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

    // Iterate over any bodies in the root component.
    double totalVolume = .0;
    Ptr<BRepBodies> bodies = rootComp->bRepBodies();
    if (!bodies)
        return false;
    for (size_t j = 0; j < bodies->count(); ++j)
    {
        Ptr<BRepBody> body = bodies->item(j);
        if (!body)
            return false;

        // Get the volume of the current body and add it to the total.
        totalVolume += body->volume();
    }

    // Iterate through all of the occurrences in the assembly.
    Ptr<OccurrenceList> occList = rootComp->allOccurrences();
    if (!occList)
        return false;
    for (size_t i = 0; i < occList->count(); ++i)
    {
        Ptr<Occurrence> occ = occList->item(i);
        if (!occ)
            return false;

        // Get the associated component.
        Ptr<Component> comp = occ->component();
        if (!comp)
            return false;

        // Iterate over all of the bodies within the component.
        Ptr<BRepBodies> compBodies = comp->bRepBodies();
        if (!compBodies)
            return false;
        for (size_t j = 0; j < compBodies->count(); ++j)
        {
            Ptr<BRepBody> body = compBodies->item(j);
            if (!body)
                return false;

            // Get the volume of the current body and add it to the total.
            totalVolume += body->volume();
        }
    }

    // Format a string to display the volume using the default distance units.
    Ptr<UnitsManager> unitMgr = product->unitsManager();
    if (!unitMgr)
        return false;

     std::string result = unitMgr->formatValue(totalVolume, unitMgr->defaultLengthUnits() + "^3");
     ui->messageBox("The volume of the entire asembly is: " + result);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |