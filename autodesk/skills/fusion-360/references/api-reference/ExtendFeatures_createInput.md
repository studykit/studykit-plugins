# ExtendFeatures.createInput Method

Parent Object: [ExtendFeatures](ExtendFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeatures.h>

## Description

Creates an ExtendFeatureInput object. Use properties and methods on this object to define the extend feature you want to create and then use the Add method, passing in the ExtendFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeatures\_var" is a variable referencing an [ExtendFeatures](ExtendFeatures.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"extendFeatures\_var" is a variable referencing an [ExtendFeatures](ExtendFeatures.htm) object.  ```` ``` #include <Fusion/Features/ExtendFeatures.h>  // Uses no optional arguments. returnValue = extendFeatures_var->createInput(edges, distance, extendType);  // Uses optional arguments. returnValue = extendFeatures_var->createInput(edges, distance, extendType, isChainingEnabled); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ExtendFeatureInput](ExtendFeatureInput.htm) | Returns the newly created ExtendFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| edges | [ObjectCollection](ObjectCollection.htm) | The surface edges to extend. Only the outer edges from an open body can be extended. The edges must all be from the same body. Depending on the extend type there can also be some limitations on the edges being input as described below for the extendType argument. |
| distance | [ValueInput](ValueInput.htm) | ValueInput object that defines the distance to extend the face/s. Natural and Tangent Extend types require a positive distance value. Perpendicular Extend Type supports either a positive or negative value to control the direction of the extend. A positive number results in the perpendicular extension being in the same direction as the positive normal of the connected faces. |
| extendType | [SurfaceExtendTypes](SurfaceExtendTypes.htm) | The extension type to use when extending the face(s). Input edges must be connected at endpoints when Tangent or Perpendicular Extend Types are used. Input edges need not be connected when Natural Extend type is used. |
| isChainingEnabled | boolean | An optional boolean argument whose default is true. If this argument is true, all edges that are tangent or curvature continuous, and end point connected, will be found automatically and include in the set of edges to extend.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [extendFeatures.add](extendFeatures_add_Sample.htm) | Demonstrates the extendFeatures.add method. To use this sample, have a design open that contains at least one surface body. When you run the sample, you will be prompted to select an open edge of the body. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |