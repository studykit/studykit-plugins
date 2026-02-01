# Sketch Point API Sample

## Description

Demonstrates creating a new sketch point.

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

        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane.
        sketches = rootComp.sketches;
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)

        # Get sketch health state
        health = sketch.healthState
        if health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState or health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState:
            msg = sketch.errorOrWarningMessage

        # Get sketch points
        sketchPoints = sketch.sketchPoints

        # Create sketch point
        point = adsk.core.Point3D.create(1.0, 1.0, 0)
        sketchPoint = sketchPoints.add(point)

        # Move sketch point
        translation = adsk.core.Vector3D.create(1.0, 0, 0)
        sketchPoint.move(translation)

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
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchPoints.h>
#include <Fusion/Sketch/SketchPoint.h>

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

    // Get sketch health state
    adsk::fusion::FeatureHealthStates health = sketch->healthState();
    if (health == adsk::fusion::FeatureHealthStates::ErrorFeatureHealthState ||
        health == adsk::fusion::FeatureHealthStates::WarningFeatureHealthState)
    {
        std::string msg = sketch->errorOrWarningMessage();
    }

    // Get sketch texts
    Ptr<SketchPoints> sketchPoints = sketch->sketchPoints();
    if (!sketchPoints)
        return false;

    // Create sketch point
    Ptr<Point3D> point = Point3D::create(1.0, 1.0, 0);
    Ptr<SketchPoint> sketchPoint = sketchPoints->add(point);
    if (!sketchPoint)
        return false;

    // Move sketch point
    Ptr<Vector3D> translation = Vector3D::create(1.0, 0.0, 0.0);
    sketchPoint->move(translation);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |