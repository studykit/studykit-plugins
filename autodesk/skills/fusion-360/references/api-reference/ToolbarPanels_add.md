# ToolbarPanels.add Method

Parent Object: [ToolbarPanels](ToolbarPanels.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanels.h>

## Description

Creates a new ToolbarPanel. The panel is initially empty. Use the associated ToolbarControls collection to add buttons.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarPanels\_var" is a variable referencing a [ToolbarPanels](ToolbarPanels.htm) object.```` ``` # Uses no optional arguments. returnValue = toolbarPanels_var.add(id, name)  # Uses optional arguments. returnValue = toolbarPanels_var.add(id, name, positionID, isBefore) ``` ```` |

"toolbarPanels\_var" is a variable referencing a [ToolbarPanels](ToolbarPanels.htm) object.  ```` ``` #include <Core/UserInterface/ToolbarPanels.h>  // Uses no optional arguments. returnValue = toolbarPanels_var->add(id, name);  // Uses optional arguments. returnValue = toolbarPanels_var->add(id, name, positionID, isBefore); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ToolbarPanel](ToolbarPanel.htm) | Returns the newly created panel or null in the case the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The unique id for this panel. The id must be unique with respect to all of the panels. |
| name | string | The displayed name of this panel. This is the name visible in the user interface. |
| positionID | string | Specifies the id of the panel to position this panel relative to. Not setting this value indicates that the panel will be created at the end of all other panels. The isBefore parameter specifies whether to place the panel before or after this panel.   This is an optional argument whose default value is "". |
| isBefore | boolean | Specifies whether to place the panel before or after the panel specified by the positionID argument. This argument is ignored is positionID is not specified   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Customizing the UI using the API Sample](UICustomizationSample_Sample.htm) | Demonstrates how to work with tabs, panels, and command in the user interface. The full source for [C++](../ExtraFiles/UICustomizationSampleCPP.zip) and [Python](../ExtraFiles/UICustomizationSamplePython.zip) samples can be downloaded. This is especially useful for getting the resource files. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |