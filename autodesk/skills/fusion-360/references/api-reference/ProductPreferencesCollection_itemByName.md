# ProductPreferencesCollection.itemByName Method

Parent Object: [ProductPreferencesCollection](ProductPreferencesCollection.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ProductPreferencesCollection.h>

## Description

Returns the ProductPreference object with the specified name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"productPreferencesCollection\_var" is a variable referencing a [ProductPreferencesCollection](ProductPreferencesCollection.htm) object.```` ``` returnValue = productPreferencesCollection_var.itemByName(name) ``` ```` |

"productPreferencesCollection\_var" is a variable referencing a [ProductPreferencesCollection](ProductPreferencesCollection.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ProductPreferences](ProductPreferences.htm) | Returns the ProductPreferences object or null if if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the ProductPreferences to return. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |