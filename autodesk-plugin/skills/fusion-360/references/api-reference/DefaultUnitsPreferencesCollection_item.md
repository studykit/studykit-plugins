# DefaultUnitsPreferencesCollection.item Method

Parent Object: [DefaultUnitsPreferencesCollection](DefaultUnitsPreferencesCollection.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DefaultUnitsPreferencesCollection.h>

## Description

Function that returns the specified DefaultUnitPreferences object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"defaultUnitsPreferencesCollection\_var" is a variable referencing a [DefaultUnitsPreferencesCollection](DefaultUnitsPreferencesCollection.htm) object.```` ``` returnValue = defaultUnitsPreferencesCollection_var.item(index) ``` ```` |

"defaultUnitsPreferencesCollection\_var" is a variable referencing a [DefaultUnitsPreferencesCollection](DefaultUnitsPreferencesCollection.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DefaultUnitsPreferences](DefaultUnitsPreferences.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |