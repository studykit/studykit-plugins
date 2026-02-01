# CustomEventArgs.additionalInfo Property

Parent Object: [CustomEventArgs](CustomEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CustomEventArgs.h>

## Description

Information being passed to the add-in in the primary thread from the worker thread or other add-in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customEventArgs\_var" is a variable referencing a CustomEventArgs object. |

"customEventArgs\_var" is a variable referencing a CustomEventArgs object. ```` ``` #include <Core/Application/CustomEventArgs.h>  // Get the value of the property. string propertyValue = customEventArgs_var->additionalInfo(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Custom Event for Command Dialog](CustomEventCommandDialog_Sample.htm) | Demonstrates using a custom event to process getting information in the background to display in a command dialog. This is an add-in and should be copied and pasted into an add-in project. |
| [Custom Event Sample](CustomEventSample_Sample.htm) | Demonstrates the ability to call into the main thread from a worker thread. This sample is an **add-in**. To use it, use the **Scripts and Add-Ins** command to create a new add-in. Delete all of the code in the newly created add-in and replace it with the code below. Have a model open that has a parameter named "Length". Load the add-in. The add-in will change the value of the parameter every two seconds using a random value between 1 and 10. |

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |