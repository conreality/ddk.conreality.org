*****************
Device Interfaces
*****************

The Conreality DDK defines a number of abstract device interfaces for device
drivers to implement. This chapter describes the major interfaces.

.. code-block:: ocaml

   module Device : sig
     class virtual interface : object
       (* Resets the device, if applicable. *)
       method reset : unit

       (* Returns the parent device, if any. *)
       method parent : interface option

       (* Determines whether the driver requires superuser privileges. *)
       method is_privileged : bool

       (* Returns the machine-readable name of the driver. *)
       method virtual driver_name : string

       (* Returns the machine-readable name of the device. *)
       method virtual device_name : string

       (* Returns the machine-readable path of the device. *)
       method device_path : string list
     end

     type t = interface
   end

.. toctree::
   :maxdepth: 1
   :glob:

   interfaces/*
