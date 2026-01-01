# SketchSplines Object

## Description

The SketchSplines object provides access to all the objects in a sketch and provides methods to create additional sketch splines. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../SketchSplines/SketchSplines_Add.md) | Method that creates a sketch spline through the set of input points. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchSplines/SketchSplines_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchSplines/SketchSplines_Count.md) | Property that returns the number of items in this collection. |
| [Item](../SketchSplines/SketchSplines_Item.md) | Returns the specified SketchSpline object from the collection. |
| [Type](../SketchSplines/SketchSplines_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingSketch.SketchSplines](../DrawingSketch/DrawingSketch_SketchSplines.md), [PlanarSketch.SketchSplines](../PlanarSketch/PlanarSketch_SketchSplines.md), [PlanarSketchProxy.SketchSplines](../PlanarSketchProxy/PlanarSketchProxy_SketchSplines.md), [Sketch.SketchSplines](../Sketch/Sketch_SketchSplines.md), [SketchBlockDefinition.SketchSplines](../SketchBlockDefinition/SketchBlockDefinition_SketchSplines.md), [SketchBlockDefinitionProxy.SketchSplines](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_SketchSplines.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |

## Version

Introduced in version 5
