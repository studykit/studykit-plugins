# Fillet Feature Edit API Sample

## Description

Demonstrates editing a fillet feature.
To successfully run this sample you can use this [Code Samples

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

        # Get active design, root component, and timeline.
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        rootComp = design.rootComponent
        timeline = design.timeline

        # Get the first fillet feature in the root component.
        fillet: adsk.fusion.FilletFeature = rootComp.features.filletFeatures[0]

        # Roll the timeline to just before the fillet.
        fillet.timelineObject.rollTo(True)

        # Iterate over the edge sets.
        edgeSet: adsk.fusion.FilletEdgeSet = None

        # Save the edges currently used by the edge sets into a list.
        edges = []
        for edgeSet in fillet.edgeSets:
            edges.append(edgeSet.edges[0])

        # Insert the last edge into the first index and remove the last edge.
        edges.insert(0, edges[len(edges)-1])
        edges.pop(len(edges)-1)

        # Process each edge set based on its type.
        for i in range(fillet.edgeSets.count):
            edgeSet = fillet.edgeSets[i]
            if edgeSet.objectType == adsk.fusion.ConstantRadiusFilletEdgeSet.classType():
                # Change the radious of the fillet.
                constantEdgeSet: adsk.fusion.ConstantRadiusFilletEdgeSet = edgeSet
                radiusParam = constantEdgeSet.radius
                radiusParam.value = radiusParam.value / 2.0

                # Toggle the continuity type between tangent and curvature.
                if constantEdgeSet.continuity == adsk.fusion.SurfaceContinuityTypes.TangentSurfaceContinuityType:
                    constantEdgeSet.continuity = adsk.fusion.SurfaceContinuityTypes.CurvatureSurfaceContinuityType
                elif constantEdgeSet.continuity == adsk.fusion.SurfaceContinuityTypes.CurvatureSurfaceContinuityType:
                    constantEdgeSet.continuity = adsk.fusion.SurfaceContinuityTypes.TangentSurfaceContinuityType

                # Change which edge is filleted.
                newEdge = adsk.core.ObjectCollection.create()
                newEdge.add(edges[i])
                constantEdgeSet.edges = newEdge
            elif edgeSet.objectType == adsk.fusion.VariableRadiusFilletEdgeSet.classType():
                variableEdgeSet: adsk.fusion.VariableRadiusFilletEdgeSet = edgeSet

                # Swap the values of the start and end radii.
                startRadiusParam = variableEdgeSet.startRadius
                endRadiusParam = variableEdgeSet.endRadius
                startVal = startRadiusParam.value
                startRadiusParam.expression = endRadiusParam.expression
                endRadiusParam.value = startVal

                # Edit the mid positions.
                midPositions = variableEdgeSet.midPositions
                midRadii = variableEdgeSet.midRadii
                for j in range(0, midPositions.count):
                    # Change the position and radius of the mid positions.
                    pos = midPositions.item(j).value
                    pos = pos + ((1 - pos) * 0.25)
                    midPositions.item(j).value = pos

                    midRadii.item(j).value = midRadii.item(j).value * 1.5

                # Add a new position.
                newMidPosition = adsk.core.ValueInput.createByReal(0.25)
                newMidRadius = adsk.core.ValueInput.createByReal(startRadiusParam.value * 0.75)
                variableEdgeSet.addMidPosition(newMidPosition, newMidRadius)

                # Toggle the continuity type between tangent and curvature.
                if variableEdgeSet.continuity == adsk.fusion.SurfaceContinuityTypes.TangentSurfaceContinuityType:
                    variableEdgeSet.continuity = adsk.fusion.SurfaceContinuityTypes.CurvatureSurfaceContinuityType
                elif variableEdgeSet.continuity == adsk.fusion.SurfaceContinuityTypes.CurvatureSurfaceContinuityType:
                    variableEdgeSet.continuity = adsk.fusion.SurfaceContinuityTypes.TangentSurfaceContinuityType

                # Change which edge is filleted.
                newEdge = adsk.core.ObjectCollection.create()
                newEdge.add(edges[i])
                variableEdgeSet.edges = newEdge
            elif edgeSet.objectType == adsk.fusion.ChordLengthFilletEdgeSet.classType():
                chordLengthEdgeSet = adsk.fusion.ChordLengthFilletEdgeSet.cast(edgeSet)

                # Edit the chord length.
                chordLengthParam = chordLengthEdgeSet.chordLength
                chordLengthParam.value = chordLengthParam.value * .75

                # Edit the tangency weight.
                tangencyWeightParam = chordLengthEdgeSet.tangencyWeight
                tangencyWeightParam.value = tangencyWeightParam.value / 2

                # Toggle the continuity type between tangent and curvature.
                if chordLengthEdgeSet.continuity == adsk.fusion.SurfaceContinuityTypes.TangentSurfaceContinuityType:
                    chordLengthEdgeSet.continuity = adsk.fusion.SurfaceContinuityTypes.CurvatureSurfaceContinuityType
                elif chordLengthEdgeSet.continuity == adsk.fusion.SurfaceContinuityTypes.CurvatureSurfaceContinuityType:
                    chordLengthEdgeSet.continuity = adsk.fusion.SurfaceContinuityTypes.TangentSurfaceContinuityType

                # Change which edge is filleted.
                newEdge = adsk.core.ObjectCollection.create()
                newEdge.add(edges[i])
                chordLengthEdgeSet.edges = newEdge

        # Move the timeline back.
        timeline.moveToEnd()

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
#include <Core/Application/ObjectCollection.h>
#include <Core/Application/ValueInput.h>
#include <Core/Application/Document.h>

#include <Fusion/Fusion/Design.h>
#include <Fusion/Fusion/Timeline.h>
#include <Fusion/Fusion/TimelineObject.h>
#include <Fusion/Fusion/ModelParameter.h>
#include <Fusion/Fusion/ParameterList.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/FilletFeatures.h>
#include <Fusion/Features/FilletFeature.h>
#include <Fusion/Features/FilletFeatureInput.h>
#include <Fusion/Features/FilletEdgeSets.h>
#include <Fusion/Features/ConstantRadiusFilletEdgeSet.h>
#include <Fusion/Features/VariableRadiusFilletEdgeSet.h>
#include <Fusion/Features/ChordLengthFilletEdgeSet.h>
#include <Fusion/BRep/BRepEdge.h>

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

    // Get the timeline associated with this design
    Ptr<Timeline> timeline = design->timeline();
    if (!timeline)
        return false;

    // Get the first fillet in the design.
    Ptr<Features> features = rootComp->features();
    if (!features)
        return false;
    Ptr<FilletFeatures> fillets = features->filletFeatures();
    if (!fillets)
        return false;
    Ptr<FilletFeature> fillet = fillets->item(0);
    if (!fillet)
        return false;

    // Roll the timeline to just before the fillet.
    Ptr<TimelineObject> timelineObj = fillet->timelineObject();
    if (!timelineObj)
        return false;
    timelineObj->rollTo(true);

    // Change the corner type.
    bool isRollingBallCorner = fillet->isRollingBallCorner();
    fillet->isRollingBallCorner(!isRollingBallCorner);

    // Save the edges currently used by the edge sets into a vector so that they are
    // rotated from the their indexed position. 0 = 1, 1 = 2, 2 = 0.
    Ptr<BRepEdge> edges[3];
    for (int i = 0; i < 3; ++i)
    {
        Ptr<FilletEdgeSet> edgeSet = fillet->edgeSets()->item(i);
        if (!edgeSet)
            return false;
        Ptr<BRepEdge> edge = NULL;
        if (edgeSet->objectType() == adsk::fusion::ConstantRadiusFilletEdgeSet::classType())
        {
            Ptr<ConstantRadiusFilletEdgeSet> constRadEdgeSet = edgeSet;
            edge = constRadEdgeSet->edges()->item(0);
            if (!edge)
                return false;
        }
        else if (edgeSet->objectType() == adsk::fusion::ChordLengthFilletEdgeSet::classType())
        {
            Ptr<ChordLengthFilletEdgeSet> chordLengthEdgeSet = edgeSet;
            edge = chordLengthEdgeSet->edges()->item(0);
            if (!edge)
                return false;
        }
        else if (edgeSet->objectType() == adsk::fusion::VariableRadiusFilletEdgeSet::classType())
        {
            Ptr<VariableRadiusFilletEdgeSet> varRadEdgeSet = edgeSet;
            edge = varRadEdgeSet->edges()->item(0);
            if (!edge)
                return false;
        }

        // Reassign the edge into the new index.
        if (i == 2)
        {
            edges[0] = edge;
        }
        else
        {
            edges[i + 1] = edge;
        }
    }

    // Process each edge set based on its type.
    for (int i = 0; i < 3; ++i)
    {
        Ptr<FilletEdgeSet> edgeSet = fillet->edgeSets()->item(i);
        if (!edgeSet)
            return false;

        if (edgeSet->objectType() == adsk::fusion::ConstantRadiusFilletEdgeSet::classType())
        {
            Ptr<ConstantRadiusFilletEdgeSet> constRadEdgeSet = edgeSet;

            // Change the radius of the fillet.
            Ptr<ModelParameter> radiusParam = constRadEdgeSet->radius();
            if (!radiusParam)
                return false;
            radiusParam->value(radiusParam->value() / 2.0);

            // Toggle the continuity type between tangent and curvature.
            if (constRadEdgeSet->continuity() == adsk::fusion::SurfaceContinuityTypes::TangentSurfaceContinuityType)
            {
                constRadEdgeSet->continuity(adsk::fusion::SurfaceContinuityTypes::CurvatureSurfaceContinuityType);
            }
            else if (
                constRadEdgeSet->continuity() == adsk::fusion::SurfaceContinuityTypes::CurvatureSurfaceContinuityType)
            {
                constRadEdgeSet->continuity(adsk::fusion::SurfaceContinuityTypes::TangentSurfaceContinuityType);
            }

            // Change which edge is filleted.
            Ptr<ObjectCollection> newEdge = adsk::core::ObjectCollection::create();
            if (!newEdge)
                return false;
            newEdge->add(edges[i]);
            bool ret = constRadEdgeSet->edges(newEdge);
        }
        else if (edgeSet->objectType() == adsk::fusion::ChordLengthFilletEdgeSet::classType())
        {
            Ptr<ChordLengthFilletEdgeSet> chordLengthEdgeSet = edgeSet;

            // Edit the chord length.
            Ptr<ModelParameter> chordLengthParam = chordLengthEdgeSet->chordLength();
            if (!chordLengthParam)
                return false;
            chordLengthParam->value(chordLengthParam->value() * 0.75);

            // Edit the tangency weight.
            Ptr<ModelParameter> tangencyWeightParam = chordLengthEdgeSet->tangencyWeight();
            if (!tangencyWeightParam)
                return false;
            tangencyWeightParam->value(tangencyWeightParam->value() / 2.0);

            // Toggle the continuity type between tangent and curvature.
            if (chordLengthEdgeSet->continuity() == adsk::fusion::SurfaceContinuityTypes::TangentSurfaceContinuityType)
            {
                chordLengthEdgeSet->continuity(adsk::fusion::SurfaceContinuityTypes::CurvatureSurfaceContinuityType);
            }
            else if (
                chordLengthEdgeSet->continuity() ==
                adsk::fusion::SurfaceContinuityTypes::CurvatureSurfaceContinuityType)
            {
                chordLengthEdgeSet->continuity(adsk::fusion::SurfaceContinuityTypes::TangentSurfaceContinuityType);
            }

            // Change which edge is filleted.
            Ptr<ObjectCollection> newEdge = adsk::core::ObjectCollection::create();
            if (!newEdge)
                return false;
            newEdge->add(edges[i]);
            chordLengthEdgeSet->edges(newEdge);
        }
        else if (edgeSet->objectType() == adsk::fusion::VariableRadiusFilletEdgeSet::classType())
        {
            Ptr<VariableRadiusFilletEdgeSet> variableEdgeSet = edgeSet;

            // Swap the values of the start and end radii.
            Ptr<ModelParameter> startRadiusParam = variableEdgeSet->startRadius();
            if (!startRadiusParam)
                return false;
            Ptr<ModelParameter> endRadiusParam = variableEdgeSet->endRadius();
            if (!endRadiusParam)
                return false;
            double startVal = startRadiusParam->value();
            startRadiusParam->expression(endRadiusParam->expression());
            endRadiusParam->value(startVal);

            // Edit the mid positions.
            Ptr<ParameterList> midPositions = variableEdgeSet->midPositions();
            if (!midPositions)
                return false;
            Ptr<ParameterList> midRadii = variableEdgeSet->midRadii();
            if (!midRadii)
                return false;
            for (int j = 0; j < midPositions->count(); ++j)
            {
                // Change the position and radius of the mid positions.
                double pos = midPositions->item(j)->value();
                pos = pos + ((1 - pos) * 0.25);
                midPositions->item(j)->value(pos);

                midRadii->item(j)->value(midRadii->item(j)->value() * 1.5);
            }

            // Add a new position.
            Ptr<ValueInput> newMidPosition = adsk::core::ValueInput::createByReal(0.25);
            if (!newMidPosition)
                return false;
            Ptr<ValueInput> newMidRadius = adsk::core::ValueInput::createByReal(startRadiusParam->value() * 0.75);
            if (!newMidRadius)
                return false;
            variableEdgeSet->addMidPosition(newMidPosition, newMidRadius);

            // Toggle the continuity type between tangent and curvature.
            if (variableEdgeSet->continuity() == adsk::fusion::SurfaceContinuityTypes::TangentSurfaceContinuityType)
            {
                variableEdgeSet->continuity(adsk::fusion::SurfaceContinuityTypes::CurvatureSurfaceContinuityType);
            }
            else if (
                variableEdgeSet->continuity() == adsk::fusion::SurfaceContinuityTypes::CurvatureSurfaceContinuityType)
            {
                variableEdgeSet->continuity(adsk::fusion::SurfaceContinuityTypes::TangentSurfaceContinuityType);
            }

            // Change which edge is filleted.
            Ptr<ObjectCollection> newEdge = adsk::core::ObjectCollection::create();
            if (!newEdge)
                return false;
            newEdge->add(edges[i]);
            variableEdgeSet->edges(newEdge);
        }
    }

    // Move the timeline back.
    timeline->moveToEnd();

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |](../ExtraFiles/APISampleFilletEdgeSetData.f3d%3E%20file%3C/a%3E%20or%20create%20a%20new%20model%20with%20the%20described%20fillet%20feature.%3C/p%3E%3Cp%3E%3Col%3E%3Cli%3ECreate%20a%20new%20model%20and%20add%20a%20block%20feature.%3C/li%3E%3Cli%3ECreate%20a%20single%20fillet%20feature%20that%20defines%20three%20different%20fillets.%20The%20fillets%20need%20to%20be%20created%20in%20a%20way%20where%20they%20don%27t%20interact%20with%20one%20another.%20The%20easiest%20way%20is%20to%20create%20the%20fillets%20only%20on%20the%20vertical%20edges%20of%20the%20box.%3Col%3E%3Cli%3ECreate%20a%20constant%20radius%20fillet%20with%20a%20radius%20that%20is%20about%201/4%20the%20size%20of%20the%20box.%3C/li%3E%3Cli%3ECreate%20a%20chord%20length%20fillet%20whose%20radius%20is%20also%20about%201/4%20the%20size%20of%20the%20box.%3C/li%3E%3Cli%3ECreate%20a%20variable%20radius%20fillet%20with%20one%20intermediate%20radius%20and%20the%20radii%20are%20about%201/4%20the%20size%20of%20the%20box%20and%20less.%3C/li%3E%3C/ol%3E%3C/ol%3ERunning%20the%20sample%20script%20will%20modify%20various%20settings%20of%20each%20fillet%20and%20change%20the%20edge%20each%20fillet%20is%20applied%20to.%3C/p%3E%3Ch2%20class%3D)