# Sketch Intersect API Sample

## Description

Intersects the specified entities with the sketch plane and creates sketch geometry that represents the intersection.

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

        # Create a sketch
        sketches = rootComp.sketches
        sketch1 = sketches.add(rootComp.yZConstructionPlane)

        # Create an object collection for the points.
        points = adsk.core.ObjectCollection.create()

        # Define the points the spline with fit through.
        points.add(adsk.core.Point3D.create(-5, 0, 0))
        points.add(adsk.core.Point3D.create(5, 1, 0))
        points.add(adsk.core.Point3D.create(6, 4, 3))
        points.add(adsk.core.Point3D.create(7, 6, 6))
        points.add(adsk.core.Point3D.create(2, 3, 0))
        points.add(adsk.core.Point3D.create(0, 1, 0))

        # Create the spline.
        spline = sketch1.sketchCurves.sketchFittedSplines.add(points)

        # Get sketch lines
        sketchLines = sketch1.sketchCurves.sketchLines

        # Create sketch rectangle
        startPoint = adsk.core.Point3D.create(0, 0, 0)
        endPoint = adsk.core.Point3D.create(5.0, 5.0, 0)
        sketchLines.addTwoPointRectangle(startPoint, endPoint)

        # Get two sketch lines
        sketchLineOne = sketchLines.item(0)
        sketchLineTwo = sketchLines.item(1)

        # Get the profile
        prof = sketch1.profiles.item(0)

        # Create an extrusion input
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Define that the extent is a distance extent of 5 cm
        distance = adsk.core.ValueInput.createByReal(5.0)
        # Set the distance extent
        extInput.setDistanceExtent(False, distance)
        # Set the extrude type to be solid
        extInput.isSolid = True

        # Create the extrusion
        ext = extrudes.add(extInput)

        # Get the body with the extrude
        body = ext.bodies.item(0)

        # Get a vertex of the body
        vertex = body.vertices.item(5)

        # Get a face of the vertex
        face = vertex.faces.item(0)

        # Create perpendicular construction axis
        axes = rootComp.constructionAxes
        axisInput = axes.createInput()
        axisInput.setByPerpendicularAtPoint(face, vertex)
        axis = axes.add(axisInput)

         # Create construction point
        points = rootComp.constructionPoints
        pointInput = points.createInput()
        pointInput.setByTwoEdges(sketchLineOne, sketchLineTwo)
        point = points.add(pointInput)

        # Create construction plane
        planes = rootComp.constructionPlanes
        planeInput = planes.createInput()
        offsetValue = adsk.core.ValueInput.createByReal(3.0)
        planeInput.setByOffset(prof, offsetValue)
        plane = planes.add(planeInput)

        # Create another sketch
        sketch2 = sketches.add(rootComp.xZConstructionPlane)

        entities = []
        entities.append(body) # body
        entities.append(face) # face
        entities.append(sketchLineOne) # edge
        entities.append(vertex) # vertex
        entities.append(spline) # sketch curve
        entities.append(axis) # construction axis
        entities.append(point) # construction point
        entities.append(plane) # construction plane
        sketchEntities = sketch2.intersectWithSketchPlane(entities)

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
#include <Core/UserInterface/UserInterface.h>
#include <Core/Application/ObjectCollection.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionPlanes.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Construction/ConstructionPlaneInput.h>
#include <Fusion/Construction/ConstructionAxes.h>
#include <Fusion/Construction/ConstructionAxis.h>
#include <Fusion/Construction/ConstructionAxisInput.h>
#include <Fusion/Construction/ConstructionPoints.h>
#include <Fusion/Construction/ConstructionPointInput.h>
#include <Fusion/Construction/ConstructionPoint.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchCurves.h>
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
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/BRep/BRepBody.h>
#include <Fusion/BRep/BRepFaces.h>
#include <Fusion/BRep/BRepFace.h>
#include <Fusion/BRep/BRepVertices.h>
#include <Fusion/BRep/BRepVertex.h>

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

    // Create a new sketch on the yz plane.
    Ptr<Sketches> sketches = rootComp->sketches();
    if (!sketches)
        return false;

    Ptr<ConstructionPlane> yzPlane = rootComp->yZConstructionPlane();
    if (!yzPlane)
        return false;

    Ptr<Sketch> yzSketch = sketches->add(yzPlane);
    if (!yzSketch)
        return false;

    // Create an object collection for the points.
    Ptr<ObjectCollection> points = ObjectCollection::create();
    if (!points)
        return false;

    // Define the points the spline with fit through.
    points->add(Point3D::create(-5, 0, 0));
    points->add(Point3D::create(5, 1, 0));
    points->add(Point3D::create(6, 4, 3));
    points->add(Point3D::create(7, 6, 6));
    points->add(Point3D::create(2, 3, 0));
    points->add(Point3D::create(0, 1, 0));

    // Create the spline.
    Ptr<SketchCurves> sketchCurves = yzSketch->sketchCurves();
    if (!sketchCurves)
        return false;

    Ptr<SketchFittedSplines> splines = sketchCurves->sketchFittedSplines();
    if (!splines)
        return false;

    Ptr<SketchFittedSpline> spline = splines->add(points);
    if (!spline)
        return false;

    // Get sketch lines
    Ptr<SketchLines> sketchLines = sketchCurves->sketchLines();
    if (!sketchLines)
        return false;

    // Create sketch rectangle
    Ptr<Point3D> startPoint = Point3D::create(0, 0, 0);
    Ptr<Point3D> endPoint = Point3D::create(5.0, 5.0, 0);
    sketchLines->addTwoPointRectangle(startPoint, endPoint);

    // Get two sketch lines
    Ptr<SketchLine> sketchLineOne = sketchLines->item(0);
    Ptr<SketchLine> sketchLineTwo = sketchLines->item(1);

    // Get the profile
    Ptr<Profiles> profs = yzSketch->profiles();
    if (!profs)
        return false;

    Ptr<Profile> prof = profs->item(0);

    // Create an extrusion input
    Ptr<Features> feats = rootComp->features();
    if (!feats)
        return false;

    Ptr<ExtrudeFeatures> extrudes = feats->extrudeFeatures();
    if (!extrudes)
        return false;

    Ptr<ExtrudeFeatureInput> extInput = extrudes->createInput(prof, FeatureOperations::NewBodyFeatureOperation);

    // Define that the extent is a distance extent of 5 cm
    Ptr<ValueInput> distance = ValueInput::createByReal(5.0);
    // Set the distance extent
    extInput->setDistanceExtent(false, distance);
    // Set the extrude type to be solid
    extInput->isSolid(true);

    // Create the extrusion
    Ptr<ExtrudeFeature> ext = extrudes->add(extInput);
    if (!ext)
        return false;

    // Get the body with the extrude
    Ptr<BRepBodies> bodies = ext->bodies();
    if (!bodies)
        return false;

    Ptr<BRepBody> body = bodies->item(0);

    // Get a vertex of the body
    Ptr<BRepVertices> vertices = body->vertices();
    if (!vertices)
        return false;

    Ptr<BRepVertex> vertex = vertices->item(5);

    // Get a face of the vertex
    Ptr<BRepFaces> vertexFaces = vertex->faces();
    if (!vertexFaces)
        return false;
    Ptr<BRepFace> face = vertexFaces->item(0);

    // Get construction axes
    Ptr<ConstructionAxes> constructionAxes = rootComp->constructionAxes();
    if (!constructionAxes)
        return false;

    // Create construction axis input
    Ptr<ConstructionAxisInput> axisInput = constructionAxes->createInput();
    if (!axisInput)
        return false;

    // Create perpendicular construction axis
    axisInput->setByPerpendicularAtPoint(face, vertex);
    Ptr<ConstructionAxis> axis = constructionAxes->add(axisInput);

    // Get construction points
    Ptr<ConstructionPoints> constructionPoints = rootComp->constructionPoints();
    if (!constructionPoints)
        return false;

    // Create construction point input
    Ptr<ConstructionPointInput> pointInput = constructionPoints->createInput();
    if (!pointInput)
        return false;

    // Create construction point by two points
    pointInput->setByTwoEdges(sketchLineOne, sketchLineTwo);
    Ptr<ConstructionPoint> point = constructionPoints->add(pointInput);

    // Create construction plane
    Ptr<ConstructionPlanes> planes = rootComp->constructionPlanes();
    if (!planes)
        return false;

    // Create construction plane input
    Ptr<ConstructionPlaneInput> planeInput = planes->createInput();
    if (!planeInput)
        return false;

    // Add construction plane by offset
    Ptr<ValueInput> offsetValue = ValueInput::createByReal(3.0);
    planeInput->setByOffset(prof, offsetValue);
    Ptr<ConstructionPlane> plane = planes->add(planeInput);

    // Create a new sketch on the xz plane.
    Ptr<ConstructionPlane> xzPlane = rootComp->xZConstructionPlane();
    if (!xzPlane)
        return false;

    Ptr<Sketch> xzSketch = sketches->add(xzPlane);
    if (!xzSketch)
        return false;

    std::vector<Ptr<Base>> entities;
    entities.push_back(body);
    entities.push_back(face);
    entities.push_back(sketchLineOne);
    entities.push_back(vertex);
    entities.push_back(spline);
    entities.push_back(axis);
    entities.push_back(point);
    entities.push_back(plane);

    std::vector<Ptr<SketchEntity>> resVec = xzSketch->intersectWithSketchPlane(entities);
    if (resVec.empty())
        return false;

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |