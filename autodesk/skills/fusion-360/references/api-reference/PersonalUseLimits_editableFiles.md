# PersonalUseLimits.editableFiles Property

Parent Object: [PersonalUseLimits](PersonalUseLimits.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/PersonalUseLimits.h>

## Description

Returns a list of the DataFile objects that have been set by the user to be editable.

## Syntax

* [Python](#Python)
* [C++](#C++)

"personalUseLimits\_var" is a variable referencing a PersonalUseLimits object. |

"personalUseLimits\_var" is a variable referencing a PersonalUseLimits object. ```` ``` #include <Core/Dashboard/PersonalUseLimits.h>  // Get the value of the property. std::vector<Ptr<DataFile>> propertyValue = personalUseLimits_var->editableFiles(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [DataFile](DataFile.htm).

## Version

Introduced in version May 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |