# Sketch.redefine Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Changes which plane the sketch is based on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` returnValue = sketch_var.redefine(planarEntity) ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planarEntity | [Base](Base.htm) | A construction plane or planar face that defines the sketch plane |

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |