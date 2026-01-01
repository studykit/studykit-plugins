# ListItem Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListItem.h>

## Description

Represents a single item in a check box list or a drop-down command input.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ListItem_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](ListItem_deleteMe.htm) | Deletes this item from the list. In cases where there is the concept of active item in the list, like with a DropDownCommandInput, this method will fail if the item you're attempting to delete is currently active. You need to make another item active first, and then you can delete the item. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [icon](ListItem_icon.htm) | Gets or sets the location for the icon file used for this item in the list. This is the path to a directory that contains the image files associated with this item. This is only valid when this is a standard list or button row and is ignored for check box lists, radio control lists, and radio button groups. |
| [index](ListItem_index.htm) | Gets the index position within the list of this item. |
| [isSelected](ListItem_isSelected.htm) | Gets or sets whether this item is selected. If the item is being displayed as a check box, this controls whether it is checked or not. If it's a drop-down list or button row it controls whether this is the single selected item. Setting a drop-down list, button row item, or radio button from a group to be selected will unselect the currently selected item. For a standard list, this will get or set the single item currently selected. For a separator, setting this property is ignored and it will always return false. |
| [isSeparator](ListItem_isSeparator.htm) | Gets if this control is a separator. |
| [isValid](ListItem_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](ListItem_name.htm) | Gets or sets the name of this item as displayed in the list. If this control is a separator (isSeparator is true) or it's a button row, setting this property is ignored and getting it will return an empty string. |
| [objectType](ListItem_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentList](ListItem_parentList.htm) | Gets the parent CheckBoxListControlDefinition or object. |

## Accessed From

[ButtonRowCommandInput.selectedItem](ButtonRowCommandInput_selectedItem.htm), [DropDownCommandInput.selectedItem](DropDownCommandInput_selectedItem.htm), [ListControlDefinition.lastSelected](ListControlDefinition_lastSelected.htm), [ListItems.add](ListItems_add.htm), [ListItems.addSeparator](ListItems_addSeparator.htm), [ListItems.item](ListItems_item.htm), [RadioButtonGroupCommandInput.selectedItem](RadioButtonGroupCommandInput_selectedItem.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |