# Sketches.itemByName Method

Parent Object: [Sketches](Sketches.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketches.h>

## Description

Returns the sketch with the specified name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketches\_var" is a variable referencing a [Sketches](Sketches.htm) object.```` ``` returnValue = sketches_var.itemByName(name) ``` ```` |

"sketches\_var" is a variable referencing a [Sketches](Sketches.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Sketch](Sketch.htm) | Returns the sketch or null if there isn't a sketch with that name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the sketch as seen in the browser and the timeline. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |