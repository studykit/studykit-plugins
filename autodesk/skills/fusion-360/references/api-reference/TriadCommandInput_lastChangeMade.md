# TriadCommandInput.lastChangeMade Property

Parent Object: [TriadCommandInput](TriadCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TriadCommandInput.h>

## Description

Returns which value was most recently changed. To determine the actual change made you need to compare the transforms returned by the transform and lastTransform properties. Having information about the specific type of change made makes it easier to compare the matrices because you know what to look for.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. |

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. ```` ``` #include <Core/UserInterface/TriadCommandInput.h>  // Get the value of the property. TriadChanges propertyValue = triadCommandInput_var->lastChangeMade(); ``` ```` |

## Property Value

This is a read only property whose value is a [TriadChanges](TriadChanges.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |