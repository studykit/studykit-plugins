# DropDownCommandInput.listItems Property

Parent Object: [DropDownCommandInput](DropDownCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DropDownCommandInput.h>

## Description

Returns the ListItems object associated with this drop-down. You use this object to populate and interact with the items in the drop-down.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dropDownCommandInput\_var" is a variable referencing a DropDownCommandInput object. |

"dropDownCommandInput\_var" is a variable referencing a DropDownCommandInput object. ```` ``` #include <Core/UserInterface/DropDownCommandInput.h>  // Get the value of the property. Ptr<ListItems> propertyValue = dropDownCommandInput_var->listItems(); ``` ```` |

## Property Value

This is a read only property whose value is a [ListItems](ListItems.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |