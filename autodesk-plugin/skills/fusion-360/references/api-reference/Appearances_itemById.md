# Appearances.itemById Method

Parent Object: [Appearances](Appearances.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Appearances.h>

## Description

Returns the Appearance by it's internal unique ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearances\_var" is a variable referencing an [Appearances](Appearances.htm) object.```` ``` returnValue = appearances_var.itemById(id) ``` ```` |

"appearances\_var" is a variable referencing an [Appearances](Appearances.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Appearance](Appearance.htm) | Returns the specified appearance or null if there isn't a matching ID. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the appearance to return. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |