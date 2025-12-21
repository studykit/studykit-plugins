# ContentFamily Object

## Description

The ContentFamily object represents a content center family and provides access to the information associated with a family.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreateMember](../ContentFamily/ContentFamily_CreateMember.md) | Method that creates a member part for the specified table row. The full filename of the created member is returned. If the creation fails the FailureReason argument indicates the reason for failure. |
| [GetCustomData](../ContentFamily/ContentFamily_GetCustomData.md) | Method that gets the specified custom data from the family. The custom data is returned if it exists or this method will fail if the specified custom data does not exist. You can use the HasCustomData property to determine if custom data exists. |
| [HasCustomData](../ContentFamily/ContentFamily_HasCustomData.md) | Property indicates if the family has the specified custom data. Returns True if the data exists. |
| [Save](../ContentFamily/ContentFamily_Save.md) | Method that saves the changes that have been made to this family. This method fails if the family is not modifiable |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveCell](../ContentFamily/ContentFamily_ActiveCell.md) | Property that returns a floating cell object that caller can use for iterating the table using indices. Set the Row and Column properties on the returned object to iterate through the table. |
| [Application](../ContentFamily/ContentFamily_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ContentIdentifier](../ContentFamily/ContentFamily_ContentIdentifier.md) | Property that returns the identifier for this object. This can be used with the GetContentObject method of the ContentCenter object to obtain this object at a later time. |
| [Description](../ContentFamily/ContentFamily_Description.md) | Gets/Sets the description of this family. |
| [DesignationColumn](../ContentFamily/ContentFamily_DesignationColumn.md) | Property that returns the column representing family designation values. |
| [DisplayName](../ContentFamily/ContentFamily_DisplayName.md) | Gets/Sets the name of this family. |
| [FamilyType](../ContentFamily/ContentFamily_FamilyType.md) | Property that returns the constant that indicates what type of family this family is; kContentPartFamily or kContentFeatureFamily. |
| [FileNameColumn](../ContentFamily/ContentFamily_FileNameColumn.md) | Property that returns the column representing family file name values. |
| [InternalName](../ContentFamily/ContentFamily_InternalName.md) | Property that returns the internal name of the ContentFamily. The internal name uniquely identifies this family with respect to other families in the library and it cannot be changed so it will remain consistent. |
| [IsCustom](../ContentFamily/ContentFamily_IsCustom.md) | Property that indicates if this family is a custom or standard family. A custom family has at least one custom column and requires the additional input of the values for the custom columns and a filename when creating a member of the family. |
| [IsModifiable](../ContentFamily/ContentFamily_IsModifiable.md) | Property that indicates if this library is writable or not. Returns True in the case where the library is modifiable. |
| [LibraryInternalName](../ContentFamily/ContentFamily_LibraryInternalName.md) | Property that returns the internal name of the library this family is defined within. |
| [LibraryName](../ContentFamily/ContentFamily_LibraryName.md) | Property that returns the display name of the library this family is defined within. |
| [Manufacturer](../ContentFamily/ContentFamily_Manufacturer.md) | Gets/Sets the manufacturer of the parts within this family. |
| [MemberDirectory](../ContentFamily/ContentFamily_MemberDirectory.md) | Gets/Sets the name of the directory where family members are saved. |
| [RevisionId](../ContentFamily/ContentFamily_RevisionId.md) | Property that returns the family revision Id, which is a GUID in string format. |
| [Standard](../ContentFamily/ContentFamily_Standard.md) | Gets/Sets the standard this family is based on. |
| [StandardOrganization](../ContentFamily/ContentFamily_StandardOrganization.md) | Gets/Sets the standard organization this family is part of. |
| [StandardRevision](../ContentFamily/ContentFamily_StandardRevision.md) | Gets/Sets the standard revision this family is based on. |
| [TableColumns](../ContentFamily/ContentFamily_TableColumns.md) | Property that returns the collection of columns for the table associated with this family. |
| [TableRows](../ContentFamily/ContentFamily_TableRows.md) | Property that returns the collection of rows for the table associated with this family. |
| [Thumbnail](../ContentFamily/ContentFamily_Thumbnail.md) | Gets/Sets the image used for the thumbnail of this family. |
| [Type](../ContentFamily/ContentFamily_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ContentFamiliesEnumerator.Item](../ContentFamiliesEnumerator/ContentFamiliesEnumerator_Item.md), [ContentTableCell.Parent](../ContentTableCell/ContentTableCell_Parent.md), [ContentTableColumn.Parent](../ContentTableColumn/ContentTableColumn_Parent.md), [ContentTableRow.Parent](../ContentTableRow/ContentTableRow_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Replace content center part](../../sample-programs/ContentCenterPartReplace_Sample.md) | This sample demonstrates how to replace the content part referenced by an assembly occurrence. |
| [Place Content Center Parts](../../sample-programs/PlaceContentCenterPart_Sample.md) | Places all of the items in a specified family within an assembly. The specific family is identified by the strings where it's setting the HexHeadNode variable. |

## Version

Introduced in version 2010
