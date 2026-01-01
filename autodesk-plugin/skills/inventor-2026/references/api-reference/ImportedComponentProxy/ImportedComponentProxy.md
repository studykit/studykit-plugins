# ImportedComponentProxy Object

## Description

ImportedComponentProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../ImportedComponentProxy/ImportedComponentProxy_BreakLinkToFile.md) | Breaks the connection of the Reference Component with the file from which it was created. |
| [Delete](../ImportedComponentProxy/ImportedComponentProxy_Delete.md) | Deletes the Reference Component. |
| [GetReferenceKey](../ImportedComponentProxy/ImportedComponentProxy_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |
| [SetEndOfPart](../ImportedComponentProxy/ImportedComponentProxy_SetEndOfPart.md) | Method that repositions the end of part marker relative to the object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ImportedComponentProxy/ImportedComponentProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ImportedComponentProxy/ImportedComponentProxy_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [ContainingOccurrence](../ImportedComponentProxy/ImportedComponentProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../ImportedComponentProxy/ImportedComponentProxy_Definition.md) | Read-write property that gets and sets the ImportedComponentDefinition which defines the various inputs that were used to create the imported component. |
| [HealthStatus](../ImportedComponentProxy/ImportedComponentProxy_HealthStatus.md) | Gets the health status of this object. |
| [IsEmbedded](../ImportedComponentProxy/ImportedComponentProxy_IsEmbedded.md) | Gets whether or not the Reference Component refers to an embedded document or a linked document. |
| [LinkedToFile](../ImportedComponentProxy/ImportedComponentProxy_LinkedToFile.md) | Gets whether or not the Reference Component is still connected to the source file. |
| [Name](../ImportedComponentProxy/ImportedComponentProxy_Name.md) | Gets the name of this Reference Component within the scope of this Document. |
| [NativeObject](../ImportedComponentProxy/ImportedComponentProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../ImportedComponentProxy/ImportedComponentProxy_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [ReferencedDocumentDescriptor](../ImportedComponentProxy/ImportedComponentProxy_ReferencedDocumentDescriptor.md) | Gets the the descriptor of the document that was used to create this Reference Component. |
| [SuppressLinkToFile](../ImportedComponentProxy/ImportedComponentProxy_SuppressLinkToFile.md) | Read-write property that gets and sets whether to suppress the connection of the imported component with the file from which it was created. |
| [Type](../ImportedComponentProxy/ImportedComponentProxy_Type.md) | Gets the constant that indicates the type of this object. |

## Version

Introduced in version 2016
