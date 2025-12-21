# AssemblyDocument.GetSelectedObject Method

Parent Object: [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md)

## Description

In order to provide better handling of system resources Inventor does not load all of the data when a document is opened but delays loading information until it is needed. A common need in many programs is to have the user select vertices on parts. Instead of loading the part model in order to return the true selected Vertex, Inventor returns a GenericObject. You can use this method to obtain more information about the selected object. If it is a vertex you can get the point coordinates without forcing the entire model to be loaded, or if you do need to do additional processing that requires access to the full model you can also force that by using the "SelectedObject" argument.

## Syntax

AssemblyDocument.**GetSelectedObject**( ***Selection*** As [GenericObject](../GenericObject/GenericObject.md), ***ObjectType*** As [ObjectTypeEnum](../ObjectTypeEnum.md), ***AdditionalData*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***ContainingOccurrence*** As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md), [***SelectedObject***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Selection | [GenericObject](../GenericObject/GenericObject.md) | Input object of type GenericObject that was obtained through a selection. |
| ObjectType | [ObjectTypeEnum](../ObjectTypeEnum.md) | Output ObjectTypeEnum value that indicates the type of object selected. |
| AdditionalData | [NameValueMap](../NameValueMap/NameValueMap.md) | Output NameValueMap object that provides any additional information for the entity.  The following describes the data currently returned.  | Object Type | Name | Value | | --- | --- | --- | | Vertex | Point | Point | |
| ContainingOccurrence | [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) | Output ComponentOccurrence object that contains the entity that was selected. |
| SelectedObject | Variant | Optional output that returns the actual entity that was selected. If this argument is provided then Inventor will load whatever additional data is required from the referenced document in order to provide the entity. |

## Version

Introduced in version 2011
