# Constant Radius Fillet API Sample

## Description

Creates a constant radius fillet on the selected edge. If there are tangent contiguous edges that will also be included in the fillet.

## Code Samples

* [C++](#C++)
* [Python](#Python)

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/Application/ObjectCollection.h>
#include <Core/Application/ValueInput.h>
#include <Core/UserInterface/Selection.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/BRep/BRepEdge.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/FilletFeatureInput.h>
#include <Fusion/Features/FilletFeatures.h>
#include <Fusion/Fusion/Design.h>

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

    Ptr<Design> design = app->activeProduct();
    if (!design)
        return false;

    // Get the root component of the active design
    Ptr<Component> root = design->rootComponent();
    if (!root)
        return false;

    // Have the edge selected and add it to an ObjectCollection.
    Ptr<Selection> selection = ui->selectEntity("Select edge to fillet", "Edges");
    if (!selection)
        return false;

    Ptr<BRepEdge> edge = selection->entity();
    if (!edge)
        return false;

    Ptr<ObjectCollection> edgeCollection = ObjectCollection::create();
    if (!edgeCollection)
        return false;
    edgeCollection->add(edge);

    Ptr<Features> feats = root->features();
    if (!feats)
        return false;

    Ptr<FilletFeatures> fillets = feats->filletFeatures();
    if (!fillets)
        return false;

    Ptr<FilletFeatureInput> filletInput = fillets->createInput();
    if (!filletInput)
        return false;
    filletInput->addConstantRadiusEdgeSet(edgeCollection, ValueInput::createByString(".25 in"), true);

    Ptr<FilletFeature> fillet = fillets->add(filletInput);
    return true;
}
```

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, traceback

def createFillet():
    ui = None
    try:
        # Get the Application object.
        app = adsk.core.Application.get()

        # Get various top-level Fusion objects.
        ui  = app.userInterface
        design = app.activeProduct
        root = design.rootComponent

        # Have the edge selected and add it to an ObjectCollection.
        selection = ui.selectEntity("Select edge to fillet", "Edges")
        edge = selection.entity
        edgeCollection = adsk.core.ObjectCollection.create()
        edgeCollection.add(edge)

        # Create the FilletInput object.
        fillets = root.features.filletFeatures
        filletInput = fillets.createInput()
        filletInput.addConstantRadiusEdgeSet(edgeCollection, adsk.core.ValueInput.createByString('.25 in'), True)

        # Create the fillet.
        fillet = fillets.add(filletInput)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def main():
    createFillet()

main()
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |