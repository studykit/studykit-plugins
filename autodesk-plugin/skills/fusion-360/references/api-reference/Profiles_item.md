# Profiles.item Method

Parent Object: [Profiles](Profiles.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Profiles.h>

## Description

Function that returns the specified closed profile using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profiles\_var" is a variable referencing a [Profiles](Profiles.htm) object.```` ``` returnValue = profiles_var.item(index) ``` ```` |

"profiles\_var" is a variable referencing a [Profiles](Profiles.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Profile](Profile.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |