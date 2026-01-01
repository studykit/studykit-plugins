# Event Context Information

### Introduction to Event Context Information

The Autodesk Inventor API supports notification of many events. These events range across the entire API. Examples include notification of:

* When a file is opened or closed.* When a browser node is activated or renamed.* When the mouse position is updated or keyboard input is received.* When a view or assembly is changed.* When objects are selected.

Currently there are more than 80 types of events fired, accessible from the API.

Events are the means through which your application is made aware of and reacts to actions outside its control. Events are also the basis for user
interaction. If you want to trace mouse movement or know when a key has been pressed, your application must set up a handler for these specific events.

### The Purpose of Event Context Information

The majority of events are straightforward - they simply provide notification that something has occurred. However, there are some situations when a little more
information is required or some contextual information is helpful.

Consider when a file is dirtied, for example. The terms "dirtied" and "smudged" refer to the edit state of the document, somewhat analagous
to paper drawings that have been manually revised. If changes have occured that would cause Autodesk Inventor to ask if you wish to save the
file before exiting, that file is considered dirtied until saved. But some actions - a rebuild or the addition of client graphics, for example - do not affect
the shape of the model, but can still be considered a change, or a "smudging" of the document. It can be useful to know such contextual information when an event occurs.

### Interpreting Event Context Information

Few events provide context information. The following arguments and their content will be meaningless except for those specific events that do provide some
context.

Those that do provide context information populate most or all of the following arguments.

* *BeforeOrAfter* - Input EventTimingEnum indicating if the event notification is being fired before (kBefore) or after (kAfter) the event occurs.* *ReasonsForChange* - Input bit-encoded field indicating why the event occurred.* *Context* - Input NameValueMap object that contains additional information about the event. Think of this object as a list of names mapped to values (for example the name FileName might be paired with a qualified file reference).

Sometimes, if the notification occurs just before the event actually takes place, you have an opportunity to veto the event or specify some alternate action specific to that event. In such cases, the following argument will be present.

* *HandlingCode* ?When the event notification is fired before the event, you can often specify an alternate action using this parameter.

The reference guide identifies which events provide additional context information. Another way to determine this is to use the "locals" or "watch" window in VB to view the contents of the object in question (the NameValueMap object, for example).

### An example of Event Context Information

The following VB code sets up an event handler for the OnFileDirty event. Create a new .exe project in VB (not VBA), create a blank form, and then paste this code into the form's code module. This sample omits error checking for the sake of clarity and brevity. This code runs outside of Autodesk Inventor but expects to connect to it, and so assumes Autodesk Inventor is already running.

First, declare the FileAccessEvents object (which supports the OnFileDirty event) and the Autodesk Inventor Application object. These are global declarations and so are outside of a Sub.

``` 
 Dim WithEvents eFA As inventor.FileAccessEvents
 Dim oApp As inventor.Application
```

The following Sub is executed when the form is loaded (when the application is first run). It gets the Application object, and then the FileAccessEvents object is obtained from it.

``` 
 Private Sub Form_Load()
 Set oApp = GetObject(, "Inventor.Application")
 Set eFA = oApp.FileAccessEvents
 End Sub
```

The following Sub defines the handler for the OnFileDirty event of the FileAccessEvents object. This code is called if the OnFileDirty event is fired. Note the various arguments, including BeforeOrAfter, Context, and HandlingCode.

```
 Private Sub eFA_OnFileDirty(ByVal RelativeFileName As String, _
    ByVal LibraryName As String, CustomLogicalName() As Byte, _
    ByVal FullFileName As String, _
    ByVal DocumentObject As inventor.Document, _
    ByVal BeforeOrAfter As inventor.EventTimingEnum, _
    ByVal Context As inventor.NameValueMap, _
    HandlingCode As inventor.HandlingCodeEnum)
```

Print the filename of the file that became dirtied.

``` 
Debug.Print "  Event: OnFileDirty", RelativeFileName
```

Loop through the items in the NameValueMap, printing their name and value.

``` 
Dim I As Long
For I = 1 To Context.Count
   Debug.Print "Context: ", Context.Name(I), _
      Context.Value(Context.Name(I))
Next I
```

Print the meaning of the BeforeOrAfter enum.

``` 
 Select Case (BeforeOrAfter)
     Case kAfter
         Debug.Print " Timing: After"
     Case kBefore
         Debug.Print " Timing: After"
     Case Else
         Debug.Print " Timing: Aborted"
 End Select
```

This handler is not going to take any specific action (this is not an event we would attempt to veto) so let Autodesk Inventor know by setting HandlingCode to the appropriate HandlingCodeEnum.

``` 
 HandlingCode = kEventNotHandled
 End Sub
```

An example of an event that does make use of the HandlingCode argument is the OnFileResolution event. This is fired when Autodesk Inventor cannot find a referenced file, but before it displays an error. Developer code can handle this event and identify the required file, so the error is prevented from being displayed.

### Running the sample code

In Autodesk Inventor, open a part document. In VB, run the code. (If asked, specify the form as the starting module).

Now the OnFileDirty event handler is set up and ready to handle this one event. In Autodesk Inventor, modify the part in some way (for example, change the extent of an extrusion). The event is fired and the code prints some information to the VB "Immediate" window. If you don't have this window visible, enable it from the View > Immediate Window menu.

The information printed will be something like the following.

```
   Event: OnFileDirty   test.ipt
 Context: ReasonsForChange 1
  Timing: After
```

In this case, the OnFileDirty event was called when test.ipt was dirtied (i.e. modified). The context NameValueMap
object contained just one item, the ReasonsForChange flag (discussed in the next section). The
BeforeOrAfter EventTimingEnum indicates the notification occurred after the event took place.

### The ReasonsForChange flag

The preceding section indicates that the context NameValueMap may contain a ReasonsForChange flag. This is a bit
coded flag, whose value is comprised of any applicable CommandTypesEnum values. In
this case the value is 1, or kShapeEditCmdType, indicating the change occurred as a result of a command that affected the design intent - the shape of the model.

As another example - if the ReasonsForChange flag value was 65, this would mean that
both kShapeEditCmdType (value 1) and kReferencesChangeCmdType (value 64) apply.

### Special considerations

Since Autodesk Inventor 9, an application that is listening to both the OnFileDirty event and OnChange event should take into account Autodesk Inventor's new "smudged" state.

OnFileDirty is fired only when the document is dirtied (including as a result of adaptivity). It is not fired when the document is only smudged.

OnChange (and the corresponding application event) is fired when a document is changed. If the change would dirty the document, the event's context has a NameValueMap pair of ConsideredDirty = 1.

**Note:** There are some exceptions. The OnChange event will not be fired due to an update of a drawing or presentation document, or due to audit or migration during the opening of documents. In such cases only OnFileDirty is fired, and cannot be vetoed.

Since Autodesk Inventor 9, a PDM system Add-in should listen to the OnFileDirty event (FileAccessEvent) to check out a file due to a document change. The Add-in should use the context to determine whether the event can be vetoed.

To keep its file reference information up to date, the PDM Add-in should listen to the OnDocumentChange event. Upon receiving the event, the Add-in should examine the ReasonsForChange argument for the kReferencesChangeCmdType bit.

### Summary

The Autodesk Inventor API support notification of many events. Some of these events provide additional information, such as the timing of the event notification - whether it was fired before or after the event took place (the EventTimingEnum). A small number of events provide further information to qualify the context in which the event took place, through the NameValueMap object. Some events support the HandlingCode argument, which allows developer code to specify alternate actions other than the default.