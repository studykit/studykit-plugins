# Rip Feature Sample

## Description

Demonstrates creating a new sheet metal rip feature.

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
#include <Fusion/BRep/BRepFace.h>
#include <Fusion/BRep/BRepFaces.h>
#include <Fusion/BRep/BRepVertex.h>
#include <Fusion/BRep/BRepVertices.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/RipFeature.h>
#include <Fusion/Features/RipFeatureInput.h>
#include <Fusion/Features/RipFeatures.h>
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

    // Get rip features
    Ptr<Features> features = rootComp->features();
    if (!features)
        return false;

    Ptr<RipFeatures> ripFeatures = features->ripFeatures();
    if (!ripFeatures)
        return false;

    Ptr<BRepBodies> bodies = rootComp->bRepBodies();

    Ptr<BRepBody> body = bodies->item(0);

    Ptr<BRepEdges> edges = body->edges();

    Ptr<BRepVertices> vertices = body->vertices();

    // Create a between points rip
    Ptr<ValueInput> gapDistance = ValueInput::createByReal(1.23);

    Ptr<ValueInput> offset1 = ValueInput::createByReal(2.34);

    Ptr<RipFeatureInput> ripFeatureInput = ripFeatures->createRipFeatureInput();

    Ptr<BRepEdge> edge = edges->item(40);

    Ptr<BRepVertex> vertex = vertices->item(9);

    // Create the feature
    Ptr<RipFeature> ripFeature = ripFeatures->add(ripFeatureInput);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |