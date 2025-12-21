# PlanarSketches.AddWithOrientation Method

Parent Object: [PlanarSketches](../PlanarSketches/PlanarSketches.md)

## Description

Method that creates a new sketch based on the input planar entity and orientation information.

## Syntax

PlanarSketches.**AddWithOrientation**( ***PlanarEntity*** As Object, ***AxisEntity*** As Object, ***NaturalAxisDirection*** As Boolean, ***AxisIsX*** As Boolean, ***Origin*** As Object, [***UseFaceEdges***] As Boolean ) As [PlanarSketch](../PlanarSketch/PlanarSketch.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PlanarEntity | Object | Input object that defines the planar object the sketch is to be built on. Valid input for this argument includes planar faces and work planes. |
| AxisEntity | Object | Input object that defines the X or Y axis of the sketch plane (the AxisIsX argument defines which). Valid input includes linear edges, sketch lines from another sketch, and work axes. |
| NaturalAxisDirection | Boolean | Input Boolean that defines if the sketch plane X or Y axis is in the same direction as that defined by the input axis entity. True indicates the axis direction is in the same direction as that of the input entity. |
| AxisIsX | Boolean | Input Boolean that specifies if the axis entity defines the X or Y axis. True indicates the axis defines the X-axis. |
| Origin | Object | Input object that defines the origin of the sketch plane. Valid input is a vertex, work point, or a sketch point from another sketch. |
| UseFaceEdges | Boolean | Optional input Boolean that specifies if sketch geometry should automatically be created for all of the edges of the input face. This is the behavior when creating a sketch interactively in Autodesk Inventor. This argument is ignored in the case when PlanarEntity is a work plane. The default value of False specifies that no sketch geometry should automatically be created from the face edges. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature - Create Block with Pocket](../../sample-programs/ExtrudeFeature_Sample.md) | This sample demonstrates creating a simple solid consisting a block with a pocket. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Sketch Add Oriented](../../sample-programs/PlanarSketches_AddWithOrientation_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |

## Version

Introduced in version 5
