# Hem Feature Sample

## Description

Demonstrates creating a new sheet metal hem feature.

## Code Samples

* [C++](#C++)

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/Application/Document.h>
#include <Core/Application/ValueInput.h>
#include <Core/UserInterface/UserInterface.h>

#include <Fusion/Components/Component.h>
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/BRep/BRepBody.h>
#include <Fusion/BRep/BRepEdge.h>
#include <Fusion/BRep/BRepEdges.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/HemFeature.h>
#include <Fusion/Features/HemFeatureInput.h>
#include <Fusion/Features/HemFeatures.h>
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

    // Get hem features
    Ptr<Features> features = rootComp->features();
    if (!features)
        return false;

    Ptr<HemFeatures> hemFeatures = features->hemFeatures();
    if (!hemFeatures)
        return false;

    Ptr<BRepBodies> bodies = rootComp->bRepBodies();

    Ptr<BRepBody> body = bodies->item(0);

    Ptr<BRepEdges> edges = body->edges();

    // Create an open hem
    Ptr<ValueInput> gap = ValueInput::createByReal(0.2);

    Ptr<ValueInput> length = ValueInput::createByReal(2.0);

    Ptr<HemFeatureInput> openHemFeatureInput = hemFeatures->createHemFeatureInput();

    Ptr<BRepEdge> edge = edges->item(0);

    bool isFlipped = false;

    BendPositionTypes bendPositionType = BendPositionTypes::BendStartEdge;

    // Create the feature
    Ptr<HemFeature> openHemFeature = hemFeatures->add(openHemFeatureInput);

    // Create a rolled hem
    Ptr<ValueInput> radius = ValueInput::createByReal(0.3);

    Ptr<ValueInput> angle = ValueInput::createByReal(4.5);

    Ptr<HemFeatureInput> rolledHemFeatureInput = hemFeatures->createHemFeatureInput();

    Ptr<BRepEdge> edge = edges->item(4);

    bool isFlipped = false;

    BendPositionTypes bendPositionType = BendPositionTypes::BendStartEdge;

    // Create the feature
    Ptr<HemFeature> rolledHemFeature = hemFeatures->add(rolledHemFeatureInput);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |