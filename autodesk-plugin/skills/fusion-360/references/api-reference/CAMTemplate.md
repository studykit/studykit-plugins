# CAMTemplate Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplate.h>

## Description

Object that represents a template for a set of operations. These can be created from operations, optionally stored to files or in a library. The template can be used to re-create those operations in another document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CAMTemplate_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createEmpty](CAMTemplate_createEmpty.htm) | ![Preview](../images/TestTubeSmall.png)Create an empty CAMTemplate |
| [createFromFile](CAMTemplate_createFromFile.htm) | Create a CAMTemplate from a file on disk, i.e. Import the template file. Invalid files will produce errors |
| [createFromOperations](CAMTemplate_createFromOperations.htm) | Create a CAMTemplate from a list of Operations |
| [createFromXML](CAMTemplate_createFromXML.htm) | Creates a CAMTemplate from an XML string. Invalid template XML will produce errors |
| [createHoleTemplateFromOperations](CAMTemplate_createHoleTemplateFromOperations.htm) | Create a hole CAMTemplate from a list of hole operations. Hole templates may be used in Hole Recognition |
| [getHoleSignatureXML](CAMTemplate_getHoleSignatureXML.htm) | ![Preview](../images/TestTubeSmall.png)Convert hole signature to XML. This will be empty if this is not a hole template, or if there is no signature. |
| [save](CAMTemplate_save.htm) | Save the CAMTemplate to a file |
| [setHoleSignatureXML](CAMTemplate_setHoleSignatureXML.htm) | ![Preview](../images/TestTubeSmall.png)Provide an XML snippet to specify a hole signature. This will have no effect if this is not a hole template. This will fail if the provided snippet is not valid. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [description](CAMTemplate_description.htm) | Gets and sets the description of the template. |
| [isHoleTemplate](CAMTemplate_isHoleTemplate.htm) | Whether or not this is a hole template |
| [isValid](CAMTemplate_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](CAMTemplate_name.htm) | Gets and sets the name of the template. |
| [objectType](CAMTemplate_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [operations](CAMTemplate_operations.htm) | ![Preview](../images/TestTubeSmall.png)Expose operations. |

## Accessed From

[CAMTemplate.createEmpty](CAMTemplate_createEmpty.htm), [CAMTemplate.createFromFile](CAMTemplate_createFromFile.htm), [CAMTemplate.createFromOperations](CAMTemplate_createFromOperations.htm), [CAMTemplate.createFromXML](CAMTemplate_createFromXML.htm), [CAMTemplate.createHoleTemplateFromOperations](CAMTemplate_createHoleTemplateFromOperations.htm), [CAMTemplateLibrary.childTemplates](CAMTemplateLibrary_childTemplates.htm), [CAMTemplateLibrary.templateAtURL](CAMTemplateLibrary_templateAtURL.htm), [CreateFromCAMTemplateInput.camTemplate](CreateFromCAMTemplateInput_camTemplate.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |