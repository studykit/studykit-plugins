# Break Link API Sample

## Description

Iterates over all top-level occurrences and if it's a referenced component, it will break the link.

## Code Samples

* [C++](#C++)
* [Python](#Python)

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Components/Occurrence.h>
#include <Fusion/Components/Occurrences.h>
#include <Fusion/Components/Component.h>

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
    Ptr<Component> rootComp = design->rootComponent();
    if (!rootComp)
        return false;

    // Get the occurrences from the root component.
    Ptr<Occurrences> occurrences = rootComp->occurrences();
    if (!occurrences)
        return false;

    // Build an array of occurrences because breaking a link will cause the
    // collection to be modified and causes a problem iterating over the colection.
    std::vector<Ptr<Occurrence>> occs;
    for (int i = 0; i < occurrences->count(); ++i)
    {
        if (Ptr<Occurrence> occ = occurrences->item(i))
            occs.push_back(occ);
    }

    // Iterate through the top-level occurrences to see if any of them are external references.
    for (Ptr<Occurrence> occ : occs)
    {
        if (occ->isReferencedComponent())
        {
            occ->breakLink();
        }
    }

    return true;
}
```

|  |
| --- |
| Copy Code |

```
# Author-
# Description-
import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Build a list of occurrences because breaking a link will cause the
        # collection to be modified and causes a problem iterating over the colection.
        occs = []
        for occ in rootComp.occurrences:
            occs.append(occ)

        # Iterate through the top-level occurrences to see if any of them are external references.
        occ: adsk.fusion.Occurrence
        for occ in occs:
            if occ.isReferencedComponent:
                occ.breakLink()
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |