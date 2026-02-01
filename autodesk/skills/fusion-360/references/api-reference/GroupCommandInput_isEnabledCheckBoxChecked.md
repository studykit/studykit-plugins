# GroupCommandInput.isEnabledCheckBoxChecked Property

Parent Object: [GroupCommandInput](GroupCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/GroupCommandInput.h>

## Description

Gets or sets if the enabled check-box is checked or not. This is only valid when the isEnabledCheckBoxDisplayed property is true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"groupCommandInput\_var" is a variable referencing a GroupCommandInput object. |

"groupCommandInput\_var" is a variable referencing a GroupCommandInput object. ```` ``` #include <Core/UserInterface/GroupCommandInput.h>  // Get the value of the property. boolean propertyValue = groupCommandInput_var->isEnabledCheckBoxChecked();  // Set the value of the property, where value_var is a boolean. bool returnValue = groupCommandInput_var->isEnabledCheckBoxChecked(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |