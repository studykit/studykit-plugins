# BRepBodies.itemByName Method

Parent Object: [BRepBodies](BRepBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBodies.h>

## Description

Returns a specific body using the name of the body within the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBodies\_var" is a variable referencing a [BRepBodies](BRepBodies.htm) object.```` ``` returnValue = bRepBodies_var.itemByName(name) ``` ```` |

"bRepBodies\_var" is a variable referencing a [BRepBodies](BRepBodies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | The BRepBody or null if a body with the defined name is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the body, as seen in the browser, to return. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |