# Design.findEntityByToken Method

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Returns the entities associated with the provided token. The return is an array of entities. In most cases an array containing a single entity will be returned but there are cases where more than one entity can be returned. An example of this is where a token is obtained from a face and subsequent modeling operations cause the face to be split into two or more pieces. All of the faces that represent the original face will be returned with the first face being the most logical match to the original face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a [Design](Design.htm) object.```` ``` returnValue = design_var.findEntityByToken(entityToken) ``` ```` |

"design\_var" is a variable referencing a [Design](Design.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Base](Base.htm)[] | Returns an array of entities associated with the provided token, or an empty array in the case where there are no matches. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entityToken | string | The input entity token you want to find the matching entity for. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |