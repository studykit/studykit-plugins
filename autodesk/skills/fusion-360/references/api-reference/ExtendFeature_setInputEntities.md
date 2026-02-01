# ExtendFeature.setInputEntities Method

Parent Object: [ExtendFeature](ExtendFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeature.h>

## Description

Sets the edges for the extend feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeature\_var" is a variable referencing an [ExtendFeature](ExtendFeature.htm) object.```` ``` # Uses no optional arguments. returnValue = extendFeature_var.setInputEntities(edges)  # Uses optional arguments. returnValue = extendFeature_var.setInputEntities(edges, isChainingEnabled) ``` ```` |

"extendFeature\_var" is a variable referencing an [ExtendFeature](ExtendFeature.htm) object.  ```` ``` #include <Fusion/Features/ExtendFeature.h>  // Uses no optional arguments. returnValue = extendFeature_var->setInputEntities(edges);  // Uses optional arguments. returnValue = extendFeature_var->setInputEntities(edges, isChainingEnabled); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| edges | [ObjectCollection](ObjectCollection.htm) | The surface edges to extend. Only the surface edges from an open body can be extended. The edges must all be from the same open body. |
| isChainingEnabled | boolean | An optional boolean argument whose default is true. If this argument is set to true, all edges that are tangent or curvature continuous, and end point connected, will be found automatically and extended.   This is an optional argument whose default value is True. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |