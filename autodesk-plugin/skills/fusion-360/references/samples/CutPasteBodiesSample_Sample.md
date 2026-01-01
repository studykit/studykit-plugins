# Cut Paste Bodies API Sample

## Description

Demonstrates how to use Cut Paste Bodies related API.

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
        ui  = app.userInterface

        # Get active design
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get root component in this design
        rootComp = design.rootComponent

        # Get the first sub component
        occs = rootComp.occurrences
        subComp1 = occs.item(0).component

        # Get the second sub component
        subComp2 = occs.item(1).component

        # Get the first body in sub component 1
        bodyInSubComp1 = subComp1.bRepBodies.item(0)

        # Cut/paste body from sub component 1 to sub component 2
        cutPasteBody = subComp2.features.cutPasteBodies.add(bodyInSubComp1)

        # Cut/paste bodies from sub component2 to root component
        sourceBodies = adsk.core.ObjectCollection.create()
        for body in subComp2.bRepBodies:
            sourceBodies.add(body)

        rootComp.features.cutPasteBodies.add(sourceBodies)

        # Dump the information of Cut Paste Body in root component
        for cutPasteBody in rootComp.features.cutPasteBodies:
            cutPasteBodyInfo = 'CutPasteBody: name - {}'.format(cutPasteBody.name)
            ui.messageBox(cutPasteBodyInfo)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/UserInterface/UserInterface.h>
#include <Core/Application/Document.h>
#include <Core/Application/ObjectCollection.h>

#include <Fusion/Fusion/Design.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Components/Occurrences.h>
#include <Fusion/Components/Occurrence.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/CutPasteBodies.h>
#include <Fusion/Features/CutPasteBody.h>
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/BRep/BRepBody.h>

#include <iostream>

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

    // Get active design
    Ptr<Product> product = app->activeProduct();
    if (!product)
        return false;

    Ptr<Design> design = product;
    if (!design)
        return false;

    // Get root component in this design
    Ptr<Component> rootComp = design->rootComponent();
    if (!rootComp)
        return false;

    // Get the first sub component
    Ptr<Occurrences> occs = rootComp->occurrences();
    if (!occs)
        return false;

    Ptr<Occurrence> firstOcc = occs->item(0);
    if (!firstOcc)
        return false;

    Ptr<Component> subComp1 = firstOcc->component();
    if (!subComp1)
        return false;

    // Get the second sub component
    Ptr<Occurrence> secondOcc = occs->item(1);
    if (!secondOcc)
        return false;

    Ptr<Component> subComp2 = secondOcc->component();
    if (!subComp2)
        return false;

    // Get the first body in sub component 1
    Ptr<BRepBodies> bodiesInSubComp1 = subComp1->bRepBodies();
    if (!bodiesInSubComp1)
        return false;

    Ptr<BRepBody> bodyInSubComp1 = bodiesInSubComp1->item(0);
    if (!bodyInSubComp1)
        return false;

    // Cut/paste body from sub component 1 to sub component 2
    Ptr<Features> featuresInSubComp2 = subComp2->features();
    if (!featuresInSubComp2)
        return false;

    Ptr<CutPasteBodies> cutPasteBodiesInSubComp2 = featuresInSubComp2->cutPasteBodies();
    if (!cutPasteBodiesInSubComp2)
        return false;

    Ptr<CutPasteBody> cutPasteBody = cutPasteBodiesInSubComp2->add(bodyInSubComp1);
    if (!cutPasteBody)
        return false;

    // Cut/paste bodies from sub component to root component
    Ptr<ObjectCollection> bodyCollection = ObjectCollection::create();
    if (!bodyCollection)
        return false;

    Ptr<BRepBodies> bodiesInSubComp2 = subComp2->bRepBodies();
    if (!bodiesInSubComp2)
        return false;

    for (size_t i = 0; i < bodiesInSubComp2->count(); ++i)
        bodyCollection->add(bodiesInSubComp2->item(i));

    Ptr<Features> featuresInRoot = rootComp->features();
    if (!featuresInRoot)
        return false;

    Ptr<CutPasteBodies> cutPasteBodiesInRoot = featuresInRoot->cutPasteBodies();
    if (!cutPasteBodiesInRoot)
        return false;

    cutPasteBody = cutPasteBodiesInRoot->add(bodyCollection);
    if (!cutPasteBody)
        return false;

    // Dump the information of Cut Paste Body in root component
    for (size_t i = 0; i < cutPasteBodiesInRoot->count(); ++i)
    {
        cutPasteBody = cutPasteBodiesInRoot->item(i);
        if (!cutPasteBody)
            return false;

        std::string cutPasteBodyInfo = "CutPasteBody: name - " + cutPasteBody->name();
         ui->messageBox(cutPasteBodyInfo);
    }

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |