# ContactSets.itemByName Method

Parent Object: [ContactSets](ContactSets.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ContactSets.h>

## Description

Returns the specified contact set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"contactSets\_var" is a variable referencing a [ContactSets](ContactSets.htm) object.```` ``` returnValue = contactSets_var.itemByName(name) ``` ```` |

"contactSets\_var" is a variable referencing a [ContactSets](ContactSets.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ContactSet](ContactSet.htm) | Returns the specified contact set or null there isn't a contact set with that name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the contact set to return. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |