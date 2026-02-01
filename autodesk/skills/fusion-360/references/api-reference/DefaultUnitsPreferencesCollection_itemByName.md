# DefaultUnitsPreferencesCollection.itemByName Method

Parent Object: [DefaultUnitsPreferencesCollection](DefaultUnitsPreferencesCollection.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DefaultUnitsPreferencesCollection.h>

## Description

Returns the DefaultUnitsPreference object with the specified name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"defaultUnitsPreferencesCollection\_var" is a variable referencing a [DefaultUnitsPreferencesCollection](DefaultUnitsPreferencesCollection.htm) object.```` ``` returnValue = defaultUnitsPreferencesCollection_var.itemByName(name) ``` ```` |

"defaultUnitsPreferencesCollection\_var" is a variable referencing a [DefaultUnitsPreferencesCollection](DefaultUnitsPreferencesCollection.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DefaultUnitsPreferences](DefaultUnitsPreferences.htm) | Returns the DefaultUnitsPreference object or null if if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the DefaultUnitsPreference to return. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |