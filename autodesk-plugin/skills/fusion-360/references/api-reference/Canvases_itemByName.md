# Canvases.itemByName Method

Parent Object: [Canvases](Canvases.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvases.h>

## Description

Returns the specified canvas using the name of the canvas.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvases\_var" is a variable referencing a [Canvases](Canvases.htm) object.```` ``` returnValue = canvases_var.itemByName(name) ``` ```` |

"canvases\_var" is a variable referencing a [Canvases](Canvases.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Canvas](Canvas.htm) | Returns the specified Canvas, if it exists. Otherwise it returns null. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the canvas as seen in the browser and timeline. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |