# CommandDefinitions.addListDefinition Method

Parent Object: [CommandDefinitions](CommandDefinitions.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandDefinitions.h>

## Description

Creates a new command definition that can be used to create a list of check boxes, radio buttons, or text with an icon within a pop-up.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandDefinitions\_var" is a variable referencing a [CommandDefinitions](CommandDefinitions.htm) object.```` ``` # Uses no optional arguments. returnValue = commandDefinitions_var.addListDefinition(id, name, listControlDisplayType)  # Uses optional arguments. returnValue = commandDefinitions_var.addListDefinition(id, name, listControlDisplayType, resourceFolder) ``` ```` |

"commandDefinitions\_var" is a variable referencing a [CommandDefinitions](CommandDefinitions.htm) object.  ```` ``` #include <Core/UserInterface/CommandDefinitions.h>  // Uses no optional arguments. returnValue = commandDefinitions_var->addListDefinition(id, name, listControlDisplayType);  // Uses optional arguments. returnValue = commandDefinitions_var->addListDefinition(id, name, listControlDisplayType, resourceFolder); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CommandDefinition](CommandDefinition.htm) | Returns the created CommandDefinition object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The unique identifier for this command definition. It must be unique with respect to all other command definitions and is limited to the following set of characters, [A-Z][a-z][0-9] and \_. |
| name | string | The name displayed in the UI for the associated selected check box list control. |
| listControlDisplayType | [ListControlDisplayTypes](ListControlDisplayTypes.htm) | Specifies the type of controls to be displayed within the list. |
| resourceFolder | string | This argument defines the resource folder that contains the images used as the icon for items in the list. Icons can be defined using either PNG or SVG files. More information about icons can be found in the user manual topic [User Interface Customization](UserInterface_UM.htm#IconsForCommands).   This is an optional argument whose default value is "". |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |