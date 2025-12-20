# TransientObjects.CreateObjectCollection Method

Parent Object: [TransientObjects](../TransientObjects/TransientObjects.md)

## Description

Constructs a new ObjectCollection object. If an ObjectsEnumerator is passed in, the collection starts off containing the enumerated objects.

## Syntax

TransientObjects.**CreateObjectCollection**( [***ObjectsEnumerator***] As Variant ) As [ObjectCollection](../ObjectCollection/ObjectCollection.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ObjectsEnumerator | Variant | Input Variant that contains the enumerated objects to place in the collection. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Interference Analysis](../../sample-programs/AssemblyComponentDefinition_AnalyzeInterference_Sample.md) | This sample demonstrates the functions used to calculate interference analysis in an assembly. |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [Baseline dimension sets](../../sample-programs/BaselineDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a baseline set dimension in a drawing. |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Add assembly occurrences to a new folder](../../sample-programs/BrowserPaneObject_AddBrowserFolder_Sample.md) | Demonstrates assembly occurrences to a new folder |
| [Chain dimensions sets](../../sample-programs/ChainDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a chain dimension set in a drawing. |
| [Copy a sketch](../../sample-programs/CopySketch_Sample.md) | This sample demonstrates copying the contents of a sketch into another sketch via the API. |
| [Selectively link paramaters](../../sample-programs/DerivedParameterTables_Add2_Sample.md) | This sample demonstrates the selective linking of parameters from another Inventor file. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Finding Bend Extent (Tangent) Edges](../../sample-programs/FlatPattern_GetEdgesOfType_Sample.md) | This sample demonstrates how to retrieve the bend extent edges (a.k.a. tangent edges) associated with the selected bend edge on a flat pattern. |
| [Modify Multiple Model States Sample](../../sample-programs/ModifyMultipleModelStatesSample_Sample.md) | This sample demonstrates how to set multiple but not all model states into edit mode. |
| [OnFaceCurve creation](../../sample-programs/OnFaceCurveSample_Sample.md) | This sample demonstrates how to create a OnFaceCurve in 3D sketch. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |
| [Move sketch entities](../../sample-programs/Sketch_MoveSketchObjects_Sample.md) | This sample demonstrates the translation of all the objects on the active sketch by a certain distance. |
| [Offset a 2D sketch](../../sample-programs/Sketch_OffsetSketchEntitiesUsingDistance_Sample.md) | This sample demonstrates the creation of offsets in 2d sketches. Two ways of creating the offset are shown - one uses a distance and the other uses the input point. |
| [Create sketched symbol and leader](../../sample-programs/SketchedSymbols_AddWithLeader_Sample.md) | This sample illustrates creating sketched symbol with a leader. |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |
| [Sketch Spline](../../sample-programs/SketchSpline_Sample.md) | This sample demonstrates creating and manipulating a sketch spline. |
| [Add surface texture symbol to dimension](../../sample-programs/SurfaceTextureSymbols_Add_Sample.md) | This sample demonstrates the creation of a surface texture symbol attached to the extension line of a drawing dimension. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |