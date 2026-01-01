# Canvases.item Method

Parent Object: [Canvases](Canvases.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvases.h>

## Description

Returns the specified canvas using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvases\_var" is a variable referencing a [Canvases](Canvases.htm) object.```` ``` returnValue = canvases_var.item(index) ``` ```` |

"canvases\_var" is a variable referencing a [Canvases](Canvases.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Canvas](Canvas.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |