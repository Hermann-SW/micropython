#include "py/dynruntime.h"
#include <string.h>

STATIC mp_obj_t len(mp_obj_t str_obj) {
    unsigned l;
    mp_obj_str_get_data(str_obj, &l);
    return mp_obj_new_int(l);
}
STATIC MP_DEFINE_CONST_FUN_OBJ_1(len_obj, len);


STATIC mp_obj_t substr(mp_obj_t str_obj, mp_obj_t from_obj, mp_obj_t len_obj) {
    unsigned l;
    byte *str = mp_obj_str_get_data(str_obj, &l);
    mp_int_t from = mp_obj_get_int(from_obj);
    mp_int_t len = mp_obj_get_int(len_obj);
    if (from < 0)  from = 0;
    if (from > l)  from = l;
    if (from + len > l)  len = l - from;
    return mp_obj_new_str_of_type(&mp_type_str, str + from, len);
}
STATIC MP_DEFINE_CONST_FUN_OBJ_3(substr_obj, substr);


mp_obj_t mpy_init(mp_obj_fun_bc_t *self, size_t n_args, size_t n_kw, mp_obj_t *args) {
    MP_DYNRUNTIME_INIT_ENTRY

    mp_store_global(MP_QSTR_len, MP_OBJ_FROM_PTR(&len_obj));
    mp_store_global(MP_QSTR_substr, MP_OBJ_FROM_PTR(&substr_obj));

    MP_DYNRUNTIME_INIT_EXIT
}
