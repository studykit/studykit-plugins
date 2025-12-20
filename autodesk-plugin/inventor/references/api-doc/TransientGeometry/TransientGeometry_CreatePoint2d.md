# TransientGeometry.CreatePoint2d Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new Point2d object.

## Syntax

TransientGeometry.**CreatePoint2d**( [***XCoord***] As Double, [***YCoord***] As Double ) As [Point2d](../Point2d/Point2d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| XCoord | Double | Input Double that specifies the point's X-coordinate. |
| YCoord | Double | Input Double that specifies the Point's Y-coordinate.   This is an optional argument whose default value is 0.0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [Create BreakOpertion by Sketch Sample](../../sample-programs/CreateBreakOpertionBySketchSample_Sample.md) | This sample demonstrates how to create a break operation using a sketch. |
| [Custom Table - create](../../sample-programs/CustomTables_Sample.md) | This sample demonstrates how to create a custom table. |
| [Create a Bend Table](../../sample-programs/CustomTables_AddBendTable_Sample.md) | This sample demonstrates the creation of a bend table in a drawing from a sheet metal part. |
| [Create a Configuration Table](../../sample-programs/CustomTables_AddConfigurationTable_Sample.md) | This sample demonstrates the creation of a configuration (iPart/iAssembly) table in a drawing from a factory document. |
| [Create a drawing Excel Table](../../sample-programs/CustomTables_AddExcelTable_Sample.md) | This sample demonstrates the creation of a table based on an Excel file in a drawing. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Finding Bend Extent (Tangent) Edges](../../sample-programs/FlatPattern_GetEdgesOfType_Sample.md) | This sample demonstrates how to retrieve the bend extent edges (a.k.a. tangent edges) associated with the selected bend edge on a flat pattern. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Creating a parts list](../../sample-programs/PartsLists_Add_Sample.md) | This sample demonstrates the creation of a parts list. The parts list is placed at the top right corner of the border if one exists, else it is placed at the top right corner of the sheet. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Sketch Edit Orientation](../../sample-programs/PlanarSketch_NaturalAxisDirection_Sample.md) | This sample demonstrates modifying the orientation of a sketch. |
| [Sketch Add Oriented](../../sample-programs/PlanarSketches_AddWithOrientation_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |
| [Projection - project across parts](../../sample-programs/Sketch_AddByProjectingEntity_Sample.md) | This sample demonstrates projecting a sketch entity across parts in an assembly. To use the sample, have an assembly open that contains at least two occurrences, (parts only), and run the program. |
| [Defer sketch updates](../../sample-programs/Sketch_DeferUpdates_Sample.md) | This sample demonstrates the sketch defer update functionality. |
| [Offset a 2D sketch](../../sample-programs/Sketch_OffsetSketchEntitiesUsingDistance_Sample.md) | This sample demonstrates the creation of offsets in 2d sketches. Two ways of creating the offset are shown - one uses a distance and the other uses the input point. |
| [Sketch Lines](../../sample-programs/Sketch_SketchLines_Sample.md) | This sample demonstrates creating lines. It uses all of the various methods to create lines, both singly and as rectangles. |
| [Create sketch elliptical arc](../../sample-programs/SketchEllipticalArc_Sample.md) | This sample demonstrates creating an elliptical arc in a sketch and dimensioning its minor radius. |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |
| [Sketch Spline](../../sample-programs/SketchSpline_Sample.md) | This sample demonstrates creating and manipulating a sketch spline. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |