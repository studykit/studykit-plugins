# Properties.itemById Method

Parent Object: [Properties](Properties.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Properties.h>

## Description

Returns the specified property from the collection using the unique ID of the property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"properties\_var" is a variable referencing a [Properties](Properties.htm) object.```` ``` returnValue = properties_var.itemById(id) ``` ```` |

"properties\_var" is a variable referencing a [Properties](Properties.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Property](Property.htm) | Returns the specified property or null if the ID doesn't match a property within the collection. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The unique ID of the property. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |