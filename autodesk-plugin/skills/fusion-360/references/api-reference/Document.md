# Document Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/Document.h>

## Description

Object that represents an open document. This is the base class for all document types.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [activate](Document_activate.htm) | Causes this document to become the active document in the user interface. |
| [classType](Document_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [close](Document_close.htm) | Closes this document. |
| [save](Document_save.htm) | Saves a version of the current document. You must use the SaveAs method the first time a document is saved. You can determine if a document has been saved by checking the value of the isSaved property. |
| [saveAs](Document_saveAs.htm) | Performs a Save As on this document. This saves the currently open document to the specified location and this document becomes the saved document. If this is a new document that has never been saved you must use the SaveAs method in order to specify the location and name. You can determine if the document has been saved by checking the value of the isSaved property. |
| [saveMilestone](Document_saveMilestone.htm) | Saves the document as a new milestone. This method is not applicable when saving a document for the first time. In that case, you must use the SaveAs method. You can determine if a document has been saved by checking the value of the isSaved property. |
| [updateAllReferences](Document_updateAllReferences.htm) | Updates all out of date external references. This is equivalent to clicking the "Out of Date" button in the Quick Access Toolbar to update all out of date external references. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [allDocumentReferences](Document_allDocumentReferences.htm) | Returns a collection containing all of the documents referenced directly by this document and those referenced by all sub-assemblies. |
| [attributes](Document_attributes.htm) | Returns the collection of attributes associated with this document. |
| [creationId](Document_creationId.htm) | Returns the creation ID of this document. When a new document is created, Fusion assigns it a creation ID that will remain constant for the life of the document. The ID that is assigned is unique. However, it's possible that more than one document can have the same ID. This happens in the case where a document is copied. In this case a new document is created but an existing document is copied. It's only when a new document is created that a creation ID is generated and assigned. |
| [dataFile](Document_dataFile.htm) | Gets the DataFile that represents this document in A360. |
| [documentReferences](Document_documentReferences.htm) | Returns a collection containing the documents directly referenced by this document. |
| [isActive](Document_isActive.htm) | Gets if this document is the active document in the user interface. |
| [isModified](Document_isModified.htm) | Property that indicates if the document has been modified since it was last saved. |
| [isSaved](Document_isSaved.htm) | Property that indicates if this document has been saved or not. The initial save of a document requires that the name and location be specified and requires the saveAs method to be used. If the document has been saved then the save method can be used to save changes made. |
| [isUpToDate](Document_isUpToDate.htm) | Indicates if any external references in the assembly are out of date. This is the API equivalent to the "Out of Date" notification displayed in the Quick Access Toolbar. |
| [isValid](Document_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](Document_isVisible.htm) | Gets if a currently open document is open as visible. |
| [name](Document_name.htm) | This property gets and sets the name of the document. You can only set the name of a document before the document is saved for the first time. You can use the isSaved property to determine this. If the document has not been saved and the name is changed, the specified name will be the default name shown in the Save dialog, which the user can modify before saving the document.   If the file has been saved, this property behaves as read-only. Setting the name will fail because the name is controlled by the DataFile associated with this document. However, you can edit the name of the DataFile, which you can obtain by using the dataFile property of the document. |
| [objectType](Document_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parent](Document_parent.htm) | Returns the parent Application object. |
| [products](Document_products.htm) | Returns the products associated with this document. |
| [version](Document_version.htm) | Returns the Fusion version this document was last saved with. |

## Accessed From

[Application.activeDocument](Application_activeDocument.htm), [CAM.parentDocument](CAM_parentDocument.htm), [Design.parentDocument](Design_parentDocument.htm), [DocumentEventArgs.document](DocumentEventArgs_document.htm), [DocumentReference.parentDocument](DocumentReference_parentDocument.htm), [DocumentReference.referencedDocument](DocumentReference_referencedDocument.htm), [Documents.add](Documents_add.htm), [Documents.item](Documents_item.htm), [Documents.open](Documents_open.htm), [Drawing.parentDocument](Drawing_parentDocument.htm), [FlatPatternProduct.parentDocument](FlatPatternProduct_parentDocument.htm), [ImportManager.importToNewDocument](ImportManager_importToNewDocument.htm), [MFGDMDataEventArgs.document](MFGDMDataEventArgs_document.htm), [Product.parentDocument](Product_parentDocument.htm), [Viewport.parentDocument](Viewport_parentDocument.htm), [WorkingModel.parentDocument](WorkingModel_parentDocument.htm)

## Derived Classes

[DrawingDocument](DrawingDocument.htm), [FusionDocument](FusionDocument.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |