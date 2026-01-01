# UserInterface.progressBar Property

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Gets the ProgressBar object that can be used to display a progress bar in the lower-right corner of the Fusion window.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a UserInterface object. |

"userInterface\_var" is a variable referencing a UserInterface object. ```` ``` #include <Core/UserInterface/UserInterface.h>  // Get the value of the property. Ptr<ProgressBar> propertyValue = userInterface_var->progressBar(); ``` ```` |

## Property Value

This is a read only property whose value is a [ProgressBar](ProgressBar.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |